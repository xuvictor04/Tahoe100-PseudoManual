---
symbol: "MIR155HG"
type: "gene"
col: 13988
ensembl_id: "ENSG00000234883"
name: "MIR155 host gene"
location: "21q21.3"
module: 112
arm: "+"
pooled_cpm: 8.01
n_lines_expressing: 22
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 18
direction_downstream: 21
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# MIR155HG

*MIR155 host gene* — 21q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.66× (z +12.2, q 3e-31, up in 12 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.611× (z -4.3, q 0.008, down in 12 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (CFPAC-1 0.111×, LOX-IMVI 0.183×, A498 0.155×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LOX-IMVI 0.135×, RKO 0.245×; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LOX-IMVI 0.128×, RKO 0.119×; ⚠ cell-cycle shift, explains ~28% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 0.0564×); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.168×); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (HCT15 0.0483×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSF2]] (+0.74, fdr 7e-06), [[TNFRSF9]] (+0.69, fdr 7e-06), [[CD274]] (+0.69, fdr 7e-06).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[LINC02605]] → it (grade B ⚠); 21 go from it, the strongest it → [[LINC02605]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13988.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.66×** | +12.2 | 3e-31 | 12/19 (CFPAC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.55×** | +11.1 | 2e-26 | 13/19 (NCI-H1792, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.62×** | +8.5 | 4e-15 | 17/19 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +8.3 | 2e-14 | 2/13 (HOP62, NCI-H1792) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.35×** | +7.5 | 7e-12 | 13/19 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.31×** | +7.4 | 1e-11 | 16/19 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +6.4 | 1e-08 | 1/11 (PANC-1) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.97×** | +5.7 | 7e-07 | 13/19 (CFPAC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +5.5 | 2e-06 | 12/19 (hTERT-HPNE, NCI-H1792, …) | rises with dose | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.10×** | +5.2 | 1e-05 | 5/11 (A-172, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +4.9 | 6e-05 | 1/15 (SW 900) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.63×** | +4.3 | 9e-04 | 13/19 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +4.2 | 0.001 | 5/19 (SW 900, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +4.2 | 0.001 | 12/19 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +3.7 | 0.010 | 11/19 (HCT15, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.034 | 7/19 (HCT15, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.44×** | +3.2 | 0.039 | 11/19 (A-172, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.96×** | +3.1 | 0.057 | 10/19 (CFPAC-1, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.081 | 6/19 (HS-578T, NCI-H1792, …) | top dose only | position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.39×** | +2.9 | 0.090 | 3/19 (H4, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.87×** | +2.9 | 0.090 | 5/18 (A498, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13988.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (CFPAC-1 0.111×, LOX-IMVI 0.183×, A498 0.155×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LOX-IMVI 0.135×, RKO 0.245×; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LOX-IMVI 0.128×, RKO 0.119×; ⚠ cell-cycle shift, explains ~28% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 0.0564×); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.168×); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (HCT15 0.0483×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.611×** | -4.3 | 0.008 | 12/19 (LoVo, A498, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.675× | -3.2 | 0.28 | 3/19 (LoVo, HCT15, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 0.697× | -3.2 | 0.28 | 8/19 (CFPAC-1, A498, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.707× | -3.1 | 0.32 | 10/19 (A498, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13988. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 67.2 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -19.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 24.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0564× (z -16.0) |
| [[A498 (line)]] | wt | 15.8 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 9.49 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.93× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 47.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.111× (z -11.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 22.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.62× (z +12.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0575× (z -10.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 24.8 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.72× (z +9.6) | — |
| [[HCT15 (line)]] | alt | 7.56 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0483× (z -9.4) |
| [[J82 (line)]] | alt | 15.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 8.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.74× (z +11.1) | — |
| [[A-427 (line)]] | wt | 0.461 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.655 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.779 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.776 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.696 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.621 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.800 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.912 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.593 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.638 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.855 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.613 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.822 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.843 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.700 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.751 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.595 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13988), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSF2]] | +0.74 | +0.74 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[TNFRSF9]] | +0.69 | +0.60 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[CD274]] | +0.69 | +0.66 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[ROR1-AS1]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[SLC43A3]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[G0S2]] | +0.64 | +0.64 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[TRAF1]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[IL1A]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[NGF]] | +0.62 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[SLAMF7]] | +0.62 | +0.57 / +0.62 | both halves | 8e-06 |  |
| [[SSTR2]] | +0.61 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[CXCL8]] | +0.61 | +0.59 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 5, C 13. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02605]] | B | LINC02605 activity raises MIR155HG's level | lines that do not express LINC02605 (15) vs lines expressing it (35) | 3.08× lower at baseline in the lines without LINC02605 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000285744, FAR2, ENSG00000285517 |
| [[LINC00944]] | B | LINC00944 activity raises MIR155HG's level | lines that do not express LINC00944 (20) vs lines expressing it (30) | 2.47× lower at baseline in the lines without LINC00944 | 0.075 | ⚠ within organs, on part of the lines; also absent: RDUR, ENSG00000289600, LINC02405 |
| [[DSE]] | B | DSE activity raises MIR155HG's level | lines that do not express DSE (9) vs lines expressing it (41) | 2.52× lower at baseline in the lines without DSE | 0.084 | ⚠ within organs, on part of the lines; also absent: SGCE, WDR17, LRP12; maybe low, not absent |
| [[PKIA]] | B | PKIA activity raises MIR155HG's level | lines that do not express PKIA (22) vs lines expressing it (28) | 2.17× lower at baseline in the lines without PKIA | 0.095 | ⚠ within organs, on part of the lines; also absent: EPHA6, GALNT13, CAMK4 |
| [[C12orf50]] | B | C12orf50 activity raises MIR155HG's level | lines that do not express C12orf50 (8) vs lines expressing it (42) | 2.07× lower at baseline in the lines without C12orf50 | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195, LYPLAL1-AS1, ENSG00000237153; maybe low, not absent |
| [[G0S2]] | C | G0S2 activity raises MIR155HG's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 3.57× lower at baseline in the lines without G0S2 | 0.003 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD; co-absent with the target |
| [[FGF5]] | C | FGF5 activity raises MIR155HG's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 3.08× lower at baseline in the lines without FGF5 | 0.014 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702; co-absent with the target |
| [[BCL2A1]] | C | BCL2A1 activity raises MIR155HG's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 2.33× lower at baseline in the lines without BCL2A1 | 0.017 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1; co-absent with the target |
| [[PSG4]] | C | PSG4 activity raises MIR155HG's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 3.50× lower at baseline in the lines without PSG4 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5; co-absent with the target |
| [[IRAG2]] | C | IRAG2 activity raises MIR155HG's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 4.13× lower at baseline in the lines without IRAG2 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411; co-absent with the target |
| [[SLC43A3]] | C | SLC43A3 activity raises MIR155HG's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 3.11× lower at baseline in the lines without SLC43A3 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261; co-absent with the target |
| [[RRAD]] | C | RRAD activity raises MIR155HG's level | lines that do not express RRAD (31) vs lines expressing it (19) | 2.35× lower at baseline in the lines without RRAD | 0.053 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 11, C 10. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02605]] | B | MIR155HG activity raises LINC02605's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 2.69× lower at baseline in the lines without MIR155HG | 0.003 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA |
| [[HMGN2P46]] | B | MIR155HG activity raises HMGN2P46's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 2.96× lower at baseline in the lines without MIR155HG | 0.021 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA |
| [[GEM]] | B | MIR155HG activity raises GEM's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 2.37× lower at baseline in the lines without MIR155HG | 0.025 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA |
| [[DSE]] | B | MIR155HG activity raises DSE's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 2.14× lower at baseline in the lines without MIR155HG | 0.033 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA |
| [[ARFGEF1]] | B | MIR155HG activity raises ARFGEF1's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 1.25× lower at baseline in the lines without MIR155HG | 0.036 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA |
| [[PKIA]] | B | MIR155HG activity raises PKIA's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 2.48× lower at baseline in the lines without MIR155HG | 0.040 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA |
| [[CYRIA]] | B | MIR155HG activity raises CYRIA's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 2.26× lower at baseline in the lines without MIR155HG | 0.059 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA |
| [[CD47]] | B | MIR155HG activity raises CD47's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 1.72× lower at baseline in the lines without MIR155HG | 0.064 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA |
| [[ADORA2A]] | B | MIR155HG activity strengthens ADORA2A's drug response | lines that do not express MIR155HG (26) vs lines expressing it (19) | the lines without MIR155HG respond 0.48× as strongly (z diff +1.02); strongest at Homoharringtonine 5 µM: 1.32x vs 2.96x (z diff +4.0) | 0.069 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA; target measured in part of the lines; artifact flags |
| [[SSTR2]] | B | MIR155HG activity raises SSTR2's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 1.47× lower at baseline in the lines without MIR155HG | 0.082 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA |
| [[DUSP10]] | B | MIR155HG activity raises DUSP10's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 2.06× lower at baseline in the lines without MIR155HG | 0.089 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA |
| [[G0S2]] | C | MIR155HG activity raises G0S2's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 5.19× lower at baseline in the lines without MIR155HG | 7e-04 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA; co-absent with the target |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.1, 1.6); signed map (41.9, 12.9). **Vector** length 65.6, 20.3% of its response variance represented; |z| ≥ 3 in 542 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.54 to 11); *Interleukin-10 signaling* (reactome, mean cos +0.56 to 5); *KRAS signaling up* (hallmark, mean cos +0.53 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.2 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.1 | +7.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +12.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.3 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +3.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +2.5 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -1.2 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -1.8 | -1.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | MIR155 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 21q21.3 — chr21:25,561,810-25,575,168 (+) |
| Ensembl biotype | lncRNA |
| Also known as | BIC, BIC-155, miPEP155, NCRNA00172, LncRNA-SERB; previously MIRHG2 |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [C0HMA1](https://www.uniprot.org/uniprotkb/C0HMA1) (HSPA8-interacting micropeptide miPEP155):

> Negatively regulates MHC class II antigen presentation in dendritic cells by interacting with the molecular chaperone HSPA8 and impairing its role in lysosomal antigen transport. Does not regulate the levels or activity of the MIR155HG microRNA from which miPEP155 is derived.

**Summary**, from NCBI Gene [114614](https://www.ncbi.nlm.nih.gov/gene/114614):

> This gene represents a microRNA host gene. The long RNA transcribed from this gene is expressed at high levels in lymphoma and may function as an oncogene. [provided by RefSeq, Dec 2017]

**Accessions** — [HGNC:35460](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:35460) · Entrez [114614](https://www.ncbi.nlm.nih.gov/gene/114614) · UniProt [C0HMA1](https://www.uniprot.org/uniprotkb/C0HMA1) · Ensembl [ENSG00000234883](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234883)

## Data

Gene col 13988: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13988); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13988, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13988]; `tensor/DDL_lfc|DDL_z.npy` [13988]; `embed/gene_vectors.npy` [13988]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13988 or target_col == 13988). Every well: [[MIR155HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR155HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
