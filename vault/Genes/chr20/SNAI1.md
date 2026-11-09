---
symbol: "SNAI1"
type: "gene"
col: 4503
ensembl_id: "ENSG00000124216"
name: "snail family transcriptional repressor 1"
location: "20q13.13"
module: 93
arm: "+"
pooled_cpm: 5.64
n_lines_expressing: 42
n_dd_up: 37
n_dd_down: 4
n_dd_up_clean: 22
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# SNAI1

*snail family transcriptional repressor 1* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.05× (z +21.3, q 0e+00, up in 31 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 0.5 µM: 0.588× (z -4.5, q 0.005, down in 18 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FSCN1]] (+0.66, fdr 1e-05), [[NDRG1]] (+0.66, fdr 3e-05), [[TNFSF9]] (+0.65, fdr 7e-06); moves opposite to [[MRRF]] (-0.55, fdr 2e-04), [[TRAPPC8]] (-0.54, fdr 8e-05), [[QRSL1]] (-0.53, fdr 3e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CRABP2]] → it (grade B ⚠); 4 go from it, the strongest it → [[ARF4-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4503.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.05×** | +21.3 | 0e+00 | 31/32 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **9.17×** | +18.6 | 0e+00 | 38/39 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **7.20×** | +16.5 | 0e+00 | 35/38 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **4.95×** | +13.4 | 1e-38 | 36/37 (SW480, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.03×** | +13.1 | 4e-37 | 28/35 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.68×** | +11.7 | 2e-29 | 35/39 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.74×** | +8.4 | 3e-15 | 26/37 (SW480, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.62×** | +8.1 | 6e-14 | 26/39 (NCI-H460, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.46×** | +7.5 | 3e-12 | 26/39 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.44×** | +7.5 | 5e-12 | 30/35 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.43×** | +7.4 | 6e-12 | 25/35 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **2.22×** | +6.7 | 1e-09 | 6/19 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.96×** | +5.6 | 1e-06 | 7/19 (NCI-H1792, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.53×** | +5.5 | 1e-06 | 7/13 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **3.44×** | +5.4 | 3e-06 | 17/38 (PANC-1, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +5.2 | 5e-06 | 11/39 (MIA PaCa-2, NCI-H2347, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.76×** | +4.7 | 7e-05 | 14/37 (KATO III, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.70×** | +4.4 | 2e-04 | 13/37 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.64×** | +3.9 | 0.002 | 11/35 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.91×** | +3.9 | 0.002 | 7/37 (SW480, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4503.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.588×** | -4.5 | 0.005 | 18/37 (H4, HOP62, …) | all doses, flat | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.639×** | -3.8 | 0.046 | 11/37 (HOP62, NCI-H2030, …) | all doses, flat | position effect removed |
| [[Vortioxetine (drug)]] 0.5 µM |  | **0.662×** | -3.5 | 0.095 | 4/37 (HepG2/C3A, RKO, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.665×** | -3.4 | 0.095 | 13/39 (Hs 766T, Panc 03.27, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 0.682× | -3.2 | 0.14 | 5/38 (Panc 03.27, A498, …) | rises with dose | position effect removed |
| [[Carbamazepine (drug)]] 0.5 µM |  | 0.694× | -3.1 | 0.17 | 9/37 (C32, A549, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.769× | -3.1 | 0.17 | 7/38 (C32, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Brimonidine (drug)]] 5 µM |  | 0.700× | -3.0 | 0.17 | 5/39 (LoVo, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.76 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4503. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.37 | 4 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.57× (z +12.6) | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.127× (z -9.1) |
| [[A498 (line)]] | wt | 25.4 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.0834× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change |
| [[NCI-H460 (line)]] | wt | 3.84 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.51× (z +11.5) | — |
| [[CFPAC-1 (line)]] | alt | 4.09 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +10.1) | [[Temsirolimus (drug)]] 0.05 µM 0.0527× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 6.87 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.54× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 4.76 | 2 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 12.4× (z +8.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 12.3× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 12.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change |
| [[A549 (line)]] | wt | 3.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.6× (z +11.3) | — |
| [[HEC-1-A (line)]] | alt | 1.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.6× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 2.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.3× (z +9.4) | — |
| [[KATO III (line)]] | alt | 2.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +9.5) | — |
| [[LoVo (line)]] | wt | 6.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.09× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.1× (z +11.9) | — |
| [[Panc 03.27 (line)]] | alt | 2.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.4× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 6.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +10.3) | — |
| [[RKO (line)]] | wt | 6.28 | 0 | 1 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0743× (z -8.7) ⚠ toxic |
| [[SW1417 (line)]] | alt | 18.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +9.6) | — |
| [[A-172 (line)]] | wt | 0.854 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.984 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.910 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.714 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.543 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.974 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.925 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4503), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FSCN1]] | +0.66 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[NDRG1]] | +0.66 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[TNFSF9]] | +0.65 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[HAP1]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[SAMD14]] | +0.65 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[TUBB3]] | +0.64 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[RGS16]] | +0.63 | +0.44 / +0.72 | both halves | 3e-05 |  |
| [[LGMN]] | +0.62 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[MIR9-1HG]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[EIF4A3]] | +0.62 | +0.43 / +0.63 | both halves | 4e-05 |  |
| [[TENT5C]] | +0.61 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[NPAS1]] | +0.60 | +0.51 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRRF]] | -0.55 | -0.31 / -0.58 | both halves | 2e-04 |  |
| [[TRAPPC8]] | -0.54 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[QRSL1]] | -0.53 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[NDUFS1]] | -0.52 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[TMEM209]] | -0.51 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[PAIP1]] | -0.50 | -0.37 / -0.48 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRABP2]] | B | CRABP2 activity raises SNAI1's level | lines that do not express CRABP2 (24) vs lines expressing it (26) | 1.94× lower at baseline in the lines without CRABP2 | 0.019 | ⚠ within organs, on part of the lines; also absent: ESPN, ACP7, HAS2 |
| [[TPBG]] | B | TPBG activity lowers SNAI1's level | lines that do not express TPBG (10) vs lines expressing it (40) | 1.51× higher at baseline in the lines without TPBG | 0.028 | ⚠ within organs, on part of the lines |
| [[CFAP45]] | B | CFAP45 activity lowers SNAI1's level | lines that do not express CFAP45 (6) vs lines expressing it (44) | 1.49× higher at baseline in the lines without CFAP45 | 0.069 | ⚠ within organs, on part of the lines; also absent: STAMBPL1, RNASEL, RUNX1; maybe low, not absent |
| [[ZCCHC24]] | B | ZCCHC24 activity raises SNAI1's level | lines that do not express ZCCHC24 (5) vs lines expressing it (45) | 1.80× lower at baseline in the lines without ZCCHC24 | 0.093 | ⚠ within organs, on part of the lines; also absent: CNTNAP1, KIF17, SLC29A4; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARF4-AS1]] | B | SNAI1 activity raises ARF4-AS1's level | lines that do not express SNAI1 (8) vs lines expressing it (42) | 1.29× lower at baseline in the lines without SNAI1 | 0.037 | ⚠ within organs, on part of the lines; also absent: TNFSF9; maybe low, not absent |
| [[LINC00887]] | B | SNAI1 activity raises LINC00887's level | lines that do not express SNAI1 (8) vs lines expressing it (42) | 1.87× lower at baseline in the lines without SNAI1 | 0.062 | ⚠ within organs, on part of the lines; also absent: TNFSF9; maybe low, not absent |
| [[TMEM209]] | B | SNAI1 activity raises TMEM209's level | lines that do not express SNAI1 (8) vs lines expressing it (42) | 1.14× lower at baseline in the lines without SNAI1 | 0.079 | ⚠ within organs, on part of the lines; also absent: TNFSF9; maybe low, not absent |
| [[OAT]] | B | SNAI1 activity raises OAT's level | lines that do not express SNAI1 (8) vs lines expressing it (42) | 2.20× lower at baseline in the lines without SNAI1 | 0.095 | ⚠ within organs, on part of the lines; also absent: TNFSF9; maybe low, not absent |

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.690). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.1, -26.6); signed map (1.8, 18.8). **Vector** length 67.9, 12.9% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +11.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +21.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +8.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.7 | +7.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +2.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.4 | +0.8 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +1.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -1.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.9 | -4.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.6 | -3.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | snail family transcriptional repressor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:49,982,980-49,988,886 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SNA, SLUGH2, SNAH, SNAIL1, SNAIL |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SNAG transcriptional repressors |
| Reactome | 18 pathways, smallest: Epithelial-Mesenchymal Transition (EMT) during gastrulation; Regulation of CDH11 gene transcription; Regulation of CDH11 Expression and Function |
| Matched by | ensembl_id |

**Function**, from UniProt [O95863](https://www.uniprot.org/uniprotkb/O95863) (Zinc finger protein SNAI1):

> Involved in induction of the epithelial to mesenchymal transition (EMT), formation and maintenance of embryonic mesoderm, growth arrest, survival and cell migration. Binds to 3 E-boxes of the E-cadherin/CDH1 gene promoter and to the promoters of CLDN7 and KRT8 and, in association with histone demethylase KDM1A which it recruits to the promoters, causes a decrease in dimethylated H3K4 levels and represses transcription. The N-terminal SNAG domain competes with histone H3 for the same binding …

**Summary**, from NCBI Gene [6615](https://www.ncbi.nlm.nih.gov/gene/6615):

> The Drosophila embryonic protein snail is a zinc finger transcriptional repressor which downregulates the expression of ectodermal genes within the mesoderm. The nuclear protein encoded by this gene is structurally similar to the Drosophila snail protein, and is also thought to be critical for mesoderm formation in the developing embryo. At least two variants of a similar processed pseudogene have been found on chromosome 2. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11128](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11128) · Entrez [6615](https://www.ncbi.nlm.nih.gov/gene/6615) · UniProt [O95863](https://www.uniprot.org/uniprotkb/O95863) · Ensembl [ENSG00000124216](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124216)

## Data

Gene col 4503: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4503); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4503, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4503]; `tensor/DDL_lfc|DDL_z.npy` [4503]; `embed/gene_vectors.npy` [4503]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4503 or target_col == 4503). Every well: [[SNAI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNAI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
