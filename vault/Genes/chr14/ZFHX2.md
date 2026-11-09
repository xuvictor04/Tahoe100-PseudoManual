---
symbol: "ZFHX2"
type: "gene"
col: 5855
ensembl_id: "ENSG00000136367"
name: "zinc finger homeobox 2"
location: "14q11.2"
module: 16
arm: "+"
pooled_cpm: 8.39
n_lines_expressing: 47
n_dd_up: 26
n_dd_down: 10
n_dd_up_clean: 25
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 9
direction_downstream: 5
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZFHX2

*zinc finger homeobox 2* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 9.13× (z +41.9, q 0e+00, up in 41 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.669× (z -5.4, q 3e-05, down in 18 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB4]] (+0.73, fdr 7e-06), [[CCDC102A]] (+0.71, fdr 7e-06), [[PBX2]] (+0.69, fdr 1e-05); moves opposite to [[NTAQ1]] (-0.64, fdr 1e-05), [[MFN1]] (-0.63, fdr 1e-05), [[SNHG30]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[MAPK8IP2]] → it (grade B ⚠); 5 go from it, the strongest it → [[SNHG30]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 2 with an alert ⚠; shown: the 15 strongest. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5855.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **9.13×** | +41.9 | 0e+00 | 41/42 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **6.77×** | +24.6 | 0e+00 | 40/42 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.01×** | +18.6 | 0e+00 | 35/41 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.89×** | +8.5 | 3e-15 | 25/44 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +5.7 | 2e-06 | 18/44 (CFPAC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.52×** | +5.6 | 2e-06 | 18/44 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.16×** | +5.4 | 6e-06 | 16/42 (NCI-H2347, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +5.3 | 1e-05 | 17/44 (CFPAC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +5.0 | 4e-05 | 12/44 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +4.8 | 9e-05 | 12/44 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.43×** | +4.8 | 1e-04 | 10/42 (RKO, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +4.5 | 3e-04 | 17/42 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +4.3 | 7e-04 | 12/43 (NCI-H23, RKO, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.37×** | +4.2 | 9e-04 | 12/43 (A-427, SW480, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.003 | 18/44 (C32, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5855.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.669×** | -5.4 | 3e-05 | 18/44 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.711×** | -4.6 | 0.001 | 14/44 (PANC-1, A-427, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.729×** | -4.3 | 0.003 | 17/44 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.713×** | -4.2 | 0.003 | 10/44 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.733×** | -4.2 | 0.003 | 17/44 (SW480, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.735×** | -4.0 | 0.006 | 16/43 (A-427, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.749×** | -3.6 | 0.024 | 9/44 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.778×** | -3.4 | 0.049 | 7/44 (NCI-H2030, H4, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.841× | -3.3 | 0.053 | 14/44 (C-33 A, NCI-H1573, …) | rises with dose |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.784×** | -3.3 | 0.055 | 10/44 (SW 900, CFPAC-1, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.787×** | -3.2 | 0.059 | 6/44 (CHP-212, RPMI-7951, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5855. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 16.3 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +9.8) | [[Ixazomib citrate (drug)]] 5 µM 0.149× (z -9.9) |
| [[A549 (line)]] | wt | 11.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.4× (z +21.8) | — |
| [[NCI-H460 (line)]] | wt | 4.57 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.1× (z +19.6) | — |
| [[PANC-1 (line)]] | alt | 6.26 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 25.4× (z +25.0) | [[Ixazomib citrate (drug)]] 5 µM 0.203× (z -8.8) |
| [[A-172 (line)]] | wt | 8.87 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.83× (z +16.8) | — |
| [[BT-474 (line)]] | alt | 11.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.53× (z +12.5) | — |
| [[C32 (line)]] | wt | 5.80 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 26.0× (z +15.9) | [[Mebendazole (drug)]] 0.5 µM 0.0640× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 14.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.37× (z +20.9) | — |
| [[NCI-H1573 (line)]] | alt | 8.37 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.65× (z +14.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.104× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 22.8 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +16.1) | [[Ixazomib citrate (drug)]] 5 µM 0.223× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 8.59 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.2× (z +20.4) | — |
| [[SK-MEL-2 (line)]] | alt | 11.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +15.8) | [[Bortezomib (drug)]] 0.05 µM 0.0677× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 9.31 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0933× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.233× (z -8.8) |
| [[A-427 (line)]] | wt | 19.0 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.106× (z -12.8) |
| [[A498 (line)]] | wt | 2.57 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.9× (z +15.1) | — |
| [[CFPAC-1 (line)]] | alt | 10.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +17.5) | — |
| [[HCT15 (line)]] | alt | 15.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +8.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0989× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~8% of this change |
| [[HOP62 (line)]] | alt | 2.88 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.1× (z +14.9) | — |
| [[LoVo (line)]] | wt | 6.31 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +16.8) | — |
| [[NCI-H1792 (line)]] | alt | 8.17 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 14.1× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 10.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.69× (z +14.5) | — |
| [[RKO (line)]] | wt | 9.99 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.10× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 4.24 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.8× (z +16.4) | — |
| [[C-33 A (line)]] | alt | 46.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -10.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 5.30 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.5× (z +11.1) | — |
| [[HS-578T (line)]] | alt | 2.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.6× (z +13.7) | — |
| [[J82 (line)]] | alt | 4.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +13.2) | — |
| [[LOX-IMVI (line)]] | wt | 2.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.7× (z +12.5) | — |
| [[NCI-H2030 (line)]] | alt | 16.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.14× (z +17.3) | — |
| [[RPMI-7951 (line)]] | alt | 4.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +10.5) | — |
| [[SW 900 (line)]] | alt | 6.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.67× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 5.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.63× (z +10.5) | — |
| [[SW48 (line)]] | wt | 8.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.0× (z +12.4) | — |
| [[AN3 CA (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5855), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB4]] | +0.73 | +0.68 / +0.63 | both halves | 7e-06 | same gene group |
| [[CCDC102A]] | +0.71 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[PBX2]] | +0.69 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[TGIF2]] | +0.69 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[DEDD]] | +0.69 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[NANOS3]] | +0.69 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[DPY19L2P2]] | +0.69 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[TEF]] | +0.69 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[MAP3K2-DT]] | +0.68 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[ZNF620]] | +0.68 | +0.73 / +0.59 | both halves | 7e-06 | same gene group |
| [[REPIN1]] | +0.67 | +0.72 / +0.56 | both halves | 1e-05 | same gene group |
| [[BTN2A2]] | +0.67 | +0.68 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NTAQ1]] | -0.64 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[MFN1]] | -0.63 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[SNHG30]] | -0.63 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[MTFR1]] | -0.62 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[SETD3]] | -0.62 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[DCUN1D2]] | -0.62 | -0.64 / -0.46 | both halves | 3e-05 |  |
| [[FBH1]] | -0.62 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[ADPGK]] | -0.61 | -0.68 / -0.51 | both halves | 1e-05 |  |
| [[PIGN]] | -0.60 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[WDR5]] | -0.60 | -0.66 / -0.46 | both halves | 3e-05 |  |
| [[RNF4]] | -0.59 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[ZCCHC17]] | -0.59 | -0.60 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAPK8IP2]] | B | MAPK8IP2 activity raises ZFHX2's level | lines that do not express MAPK8IP2 (18) vs lines expressing it (32) | 2.07× lower at baseline in the lines without MAPK8IP2 | 0.031 | ⚠ within organs, on part of the lines; also absent: AP3B2, FBXO27, LTB; maybe low, not absent |
| [[IL32]] | B | IL32 activity strengthens ZFHX2's drug response | lines that do not express IL32 (18) vs lines expressing it (26) | the lines without IL32 respond 0.62× as strongly (z diff +1.04); strongest at Harringtonine 5 µM: 3.81x vs 11x (z diff +2.2) | 0.039 | ⚠ within organs, on part of the lines; also absent: PODXL, APOL1, F3; target measured in part of the lines; artifact flags |
| [[CACHD1]] | B | CACHD1 activity raises ZFHX2's level | lines that do not express CACHD1 (7) vs lines expressing it (43) | 2.03× lower at baseline in the lines without CACHD1 | 0.041 | ⚠ within organs, on part of the lines; also absent: KCNK15-AS1 |
| [[NFATC2]] | B | NFATC2 activity lowers ZFHX2's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 1.67× higher at baseline in the lines without NFATC2 | 0.048 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[SLC2A6]] | B | SLC2A6 activity raises ZFHX2's level | lines that do not express SLC2A6 (6) vs lines expressing it (44) | 1.93× lower at baseline in the lines without SLC2A6 | 0.051 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent |
| [[SRCIN1]] | B | SRCIN1 activity raises ZFHX2's level | lines that do not express SRCIN1 (9) vs lines expressing it (41) | 2.17× lower at baseline in the lines without SRCIN1 | 0.058 | ⚠ within organs, on part of the lines; also absent: TSPAN33, PRKN |
| [[CFAP300]] | B | CFAP300 activity lowers ZFHX2's level | lines that do not express CFAP300 (18) vs lines expressing it (32) | 1.25× higher at baseline in the lines without CFAP300 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, ARID1A; also absent: MYPN, GATA3, CCL5 |
| [[SLC2A6]] | B | SLC2A6 activity strengthens ZFHX2's drug response | lines that do not express SLC2A6 (6) vs lines expressing it (38) | the lines without SLC2A6 respond 0.87× as strongly (z diff +0.58); strongest at Homoharringtonine 0.5 µM: 2.14x vs 3.98x (z diff +3.2) | 0.093 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[HHAT]] | C | HHAT activity raises ZFHX2's level | lines that do not express HHAT (4) vs lines expressing it (46) | 3.05× lower at baseline in the lines without HHAT | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC01341, C2orf92, GDAP1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNHG30]] | C | ZFHX2 activity raises SNHG30's level | lines that do not express ZFHX2 (3) vs lines expressing it (47) | 1.86× lower at baseline in the lines without ZFHX2 | 0.042 | ⚠ few lines (3 vs 47); across organs; also absent: FOXP4-AS1, ENSG00000256673, WWOX; maybe low, not absent |
| [[TEX9]] | C | ZFHX2 activity raises TEX9's level | lines that do not express ZFHX2 (3) vs lines expressing it (47) | 3.30× lower at baseline in the lines without ZFHX2 | 0.049 | ⚠ few lines (3 vs 47); across organs; also absent: FOXP4-AS1, ENSG00000256673, WWOX; maybe low, not absent; co-absent with the target |
| [[ZNF620]] | C | ZFHX2 activity raises ZNF620's level | lines that do not express ZFHX2 (3) vs lines expressing it (47) | 2.05× lower at baseline in the lines without ZFHX2 | 0.057 | ⚠ few lines (3 vs 47); across organs; also absent: FOXP4-AS1, ENSG00000256673, WWOX; maybe low, not absent |
| [[VEZF1]] | C | ZFHX2 activity raises VEZF1's level | lines that do not express ZFHX2 (3) vs lines expressing it (47) | 1.53× lower at baseline in the lines without ZFHX2 | 0.063 | ⚠ few lines (3 vs 47); across organs; also absent: FOXP4-AS1, ENSG00000256673, WWOX; maybe low, not absent |
| [[CYB5RL]] | C | ZFHX2 activity raises CYB5RL's level | lines that do not express ZFHX2 (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without ZFHX2 | 0.080 | ⚠ few lines (3 vs 47); across organs; also absent: FOXP4-AS1, ENSG00000256673, WWOX; maybe low, not absent |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.623). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (20.2, 7.6); signed map (40.2, -0.5). **Vector** length 92.9, 19.4% of its response variance represented; |z| ≥ 3 in 1,064 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.3 | +41.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +10.0 | +24.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +18.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.1 | +8.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.8 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +3.7 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | -2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -4.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.8 | -3.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:23,520,857-23,556,192 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1762, KIAA1056, ZFH-5; previously ZNF409 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Zinc fingers matrin-type; ZF class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0A1](https://www.uniprot.org/uniprotkb/Q9C0A1) (Zinc finger homeobox protein 2):

> Transcriptional regulator that is critical for the regulation of pain perception and processing of noxious stimuli.

**Summary**, from NCBI Gene [85446](https://www.ncbi.nlm.nih.gov/gene/85446):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Involved in regulation of sensory perception of pain. Located in nucleus. Implicated in Marsili syndrome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20152](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20152) · Entrez [85446](https://www.ncbi.nlm.nih.gov/gene/85446) · UniProt [Q9C0A1](https://www.uniprot.org/uniprotkb/Q9C0A1) · Ensembl [ENSG00000136367](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136367)

## Data

Gene col 5855: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5855); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5855, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5855]; `tensor/DDL_lfc|DDL_z.npy` [5855]; `embed/gene_vectors.npy` [5855]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5855 or target_col == 5855). Every well: [[ZFHX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFHX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
