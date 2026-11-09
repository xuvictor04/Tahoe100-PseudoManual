---
symbol: "BRAT1"
type: "gene"
col: 2705
ensembl_id: "ENSG00000106009"
name: "BRCA1 associated ATM activator 1"
location: "7p22.3"
module: 26
arm: "-"
pooled_cpm: 11.73
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# BRAT1

*BRCA1 associated ATM activator 1* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.04× (z +12.5, q 7e-33, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.666× (z -10.0, q 8e-21, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RSAD1]] (+0.75, fdr 7e-06), [[ACTR5]] (+0.74, fdr 7e-06), [[MAST3]] (+0.73, fdr 1e-05); moves opposite to [[CCDC90B-AS1]] (-0.74, fdr 7e-06), [[MMADHC-DT]] (-0.74, fdr 1e-05), [[LINC00571]] (-0.72, fdr 2e-05).
> It sits in the **-** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CSK]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2705.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.04×** | +12.5 | 7e-33 | 42/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.89×** | +11.1 | 3e-26 | 39/48 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.88×** | +11.0 | 5e-26 | 39/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +5.3 | 2e-05 | 18/41 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +5.1 | 4e-05 | 14/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.20× | +4.4 | 8e-04 | 14/48 (NCI-H1792, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +3.1 | 0.15 | 12/42 (C32, HepG2/C3A, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.28× | +3.1 | 0.15 | 2/45 (NCI-H1792, HCT15) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2705.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.666×** | -10.0 | 8e-21 | 32/47 (MIA PaCa-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.639×** | -7.8 | 2e-12 | 22/45 (MIA PaCa-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.642×** | -7.4 | 2e-11 | 28/47 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.682×** | -6.7 | 3e-09 | 23/47 (C32, RKO, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.714×** | -5.6 | 2e-06 | 19/46 (PANC-1, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.736×** | -5.3 | 9e-06 | 19/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.734×** | -5.2 | 2e-05 | 19/48 (SK-MEL-2, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.827×** | -4.7 | 2e-04 | 17/46 (AN3 CA, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.798×** | -3.9 | 0.006 | 12/46 (SW 900, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **0.817×** | -3.5 | 0.025 | 11/48 (MIA PaCa-2, SW48, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.824×** | -3.4 | 0.036 | 12/47 (LS 180, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.824×** | -3.4 | 0.036 | 17/47 (SW480, Hs 766T, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.825×** | -3.3 | 0.036 | 7/47 (A-172, HepG2/C3A, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.697×** | -3.3 | 0.041 | 12/48 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.831×** | -3.2 | 0.050 | 6/47 (AsPC-1, KATO III, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.832×** | -3.2 | 0.050 | 11/47 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.881× | -3.1 | 0.058 | 12/48 (SW1417, HOP62, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.839× | -2.9 | 0.098 | 7/47 (SW 1271, HS-578T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2705. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 17.4 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0699× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.258× (z -12.0) |
| [[HepG2_C3A (line)]] | wt | 5.57 | 0 | 2 | — | [[Aspirin (drug)]] 0.5 µM 0.0774× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 11.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 8.75 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.403× (z -8.6) |
| [[A-427 (line)]] | wt | 14.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -10.1) |
| [[HT-29 (line)]] | alt | 8.34 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 8.07 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.199× (z -9.0) |
| [[LoVo (line)]] | wt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 21.8 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.43× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -8.9) |
| [[PANC-1 (line)]] | alt | 16.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -10.1) |
| [[SHP-77 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.132× (z -9.2) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 13.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -9.0) |
| [[SW 900 (line)]] | alt | 8.08 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0961× (z -9.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 13.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.82× (z +9.4) | — |
| [[A-172 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2705), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSAD1]] | +0.75 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[ACTR5]] | +0.74 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[MAST3]] | +0.73 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[GTPBP3]] | +0.73 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[BRF1]] | +0.71 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[NUP160]] | +0.71 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[TSEN54]] | +0.69 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[FAM118A]] | +0.69 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[TAF5L]] | +0.68 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ASB13]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[RNF41]] | +0.68 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[L2HGDH]] | +0.68 | +0.58 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC90B-AS1]] | -0.74 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[MMADHC-DT]] | -0.74 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[LINC00571]] | -0.72 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[MZF1-AS1]] | -0.72 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[LINC01191]] | -0.72 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[BTG3-AS1]] | -0.71 | -0.66 / -0.44 | both halves | 3e-05 |  |
| [[CFAP70]] | -0.70 | -0.67 / -0.40 | both halves | 4e-05 |  |
| [[PPP1R12A-AS2]] | -0.69 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[ARRDC3-AS1]] | -0.69 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[TTC6]] | -0.69 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[LINC02542]] | -0.69 | -0.60 / -0.38 | both halves | 7e-05 |  |
| [[NQO1-DT]] | -0.69 | -0.62 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers BRAT1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NTN4]] | B | NTN4 activity lowers BRAT1's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 1.31× higher at baseline in the lines without NTN4 | 0.064 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[ZHX2]] | B | ZHX2 activity lowers BRAT1's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 1.43× higher at baseline in the lines without ZHX2 | 0.088 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |
| [[LINC00571]] | B | LINC00571 activity lowers BRAT1's level | lines that do not express LINC00571 (5) vs lines expressing it (45) | 1.55× higher at baseline in the lines without LINC00571 | 0.092 | ⚠ within organs, on part of the lines; also absent: KIFC3, NDRG1, DELEC1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises BRAT1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSK]] | C | BRAT1's natural level weakens CSK's drug response | BRAT1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.63, reverse -0.07; direction not clear | 0.074 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **-** arm (projection on the module's main direction -0.732). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-1.0, -1.7); signed map (-40.2, -13.1). **Vector** length 71.3, 11.2% of its response variance represented; |z| ≥ 3 in 921 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.4 | +11.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.1 | +12.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.8 | +11.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +0.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.3 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +2.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.7 | -6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.2 | -7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -5.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | BRCA1 associated ATM activator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:2,537,810-2,555,694 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC22916; previously C7orf27, BAAT1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PJG6](https://www.uniprot.org/uniprotkb/Q6PJG6) (Integrator complex assembly factor BRAT1):

> Component of a multiprotein complex required for the assembly of the RNA endonuclease module of the integrator complex. Associates with INTS9 and INTS11 in the cytoplasm and blocks the active site of INTS11 to inhibit the endonuclease activity of INTS11 before formation of the full integrator complex. Following dissociation of WDR73 of the complex, BRAT1 facilitates the nuclear import of the INTS9-INTS11 heterodimer. In the nucleus, INTS4 is integrated to the INTS9-INTS11 heterodimer and BRAT1 …

**Summary**, from NCBI Gene [221927](https://www.ncbi.nlm.nih.gov/gene/221927):

> The protein encoded by this ubiquitously expressed gene interacts with the tumor suppressing BRCA1 (breast cancer 1) protein and and the ATM (ataxia telangiectasia mutated) protein. ATM is thought to be a master controller of cell cycle checkpoint signalling pathways that are required for cellular responses to DNA damage such as double-strand breaks that are induced by ionizing radiation and complexes with BRCA1 in the multi-protein complex BASC (BRAC1-associated genome surveillance complex). …

**Accessions** — [HGNC:21701](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21701) · Entrez [221927](https://www.ncbi.nlm.nih.gov/gene/221927) · UniProt [Q6PJG6](https://www.uniprot.org/uniprotkb/Q6PJG6) · Ensembl [ENSG00000106009](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106009)

## Data

Gene col 2705: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2705); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2705, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2705]; `tensor/DDL_lfc|DDL_z.npy` [2705]; `embed/gene_vectors.npy` [2705]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2705 or target_col == 2705). Every well: [[BRAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
