---
symbol: "IGF2BP1"
type: "gene"
col: 8233
ensembl_id: "ENSG00000159217"
name: "insulin like growth factor 2 mRNA binding protein 1"
location: "17q21.32"
module: 95
arm: "+"
pooled_cpm: 41.99
n_lines_expressing: 27
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# IGF2BP1

*insulin like growth factor 2 mRNA binding protein 1* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.84× (z +19.7, q 0e+00, up in 16 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.219× (z -34.5, q 0e+00, down in 25 of 25 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPL]] (+0.67, fdr 2e-05), [[ANKRD18B]] (+0.66, fdr 9e-05), [[CACNA2D1]] (+0.65, fdr 9e-05); moves opposite to [[ARL6]] (-0.61, fdr 3e-05), [[WASF3]] (-0.60, fdr 3e-04), [[STX7]] (-0.60, fdr 8e-05).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SOCS2-AS1]] → it (grade B ⚠); 6 go from it, the strongest it → [[GALNT7-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8233.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +19.7 | 0e+00 | 16/25 (A-172, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +18.0 | 0e+00 | 16/25 (HepG2/C3A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +13.0 | 1e-36 | 10/24 (HepG2/C3A, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +8.9 | 5e-17 | 8/24 (HepG2/C3A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +7.3 | 4e-11 | 11/25 (SW480, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +6.3 | 4e-08 | 13/25 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +5.2 | 1e-05 | 10/25 (A549, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.20× | +4.1 | 0.002 | 5/25 (SW 1271, C-33 A, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.20×** | +3.9 | 0.007 | 5/24 (HepG2/C3A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.7 | 0.014 | 2/25 (SW480, HOP62) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.17× | +3.6 | 0.019 | 12/25 (A549, NCI-H23, …) | two highest doses | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +3.4 | 0.027 | 4/25 (NCI-H2030, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.16× | +3.3 | 0.046 | 9/25 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.2 | 0.049 | 8/25 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.15× | +3.2 | 0.056 | 4/25 (HOP62, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8233.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.219×** | -34.5 | 0e+00 | 25/25 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.251×** | -31.5 | 0e+00 | 25/25 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.306×** | -27.0 | 0e+00 | 25/25 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.554×** | -13.4 | 7e-39 | 24/25 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.482×** | -8.7 | 4e-16 | 20/25 (NCI-H23, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.787×** | -7.7 | 1e-12 | 16/25 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.795×** | -5.2 | 1e-05 | 15/25 (PANC-1, SW480, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.734×** | -3.7 | 0.017 | 12/25 (PANC-1, J82, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.862× | -3.4 | 0.043 | 13/25 (SW480, J82, …) | rises with dose |  |
| [[Pimozide (drug)]] 5 µM |  | 0.863× | -3.3 | 0.043 | 1/25 (Panc 03.27) | top dose only |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.858× | -3.3 | 0.043 | 1/25 (NCI-H1792) | top dose only | plate-row cell shift |
| [[Naproxen (drug)]] 0.05 µM |  | 0.859× | -3.2 | 0.065 | 4/25 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | 0.874× | -3.1 | 0.096 | 0/25 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8233. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 154 | 2 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +14.4) | [[Panobinostat (drug)]] 0.5 µM 0.111× (z -23.3) |
| [[PANC-1 (line)]] | alt | 97.0 | 2 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +14.3) | [[Panobinostat (drug)]] 5 µM 0.115× (z -31.6) |
| [[SNU-423 (line)]] | alt | 79.0 | 2 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.101× (z -24.7) |
| [[SW480 (line)]] | alt | 114 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0533× (z -42.4) |
| [[A-427 (line)]] | wt | 209 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.141× (z -28.0) |
| [[C-33 A (line)]] | alt | 193 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0434× (z -40.3) |
| [[NCI-H1573 (line)]] | alt | 92.5 | 2 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +11.6) | [[Panobinostat (drug)]] 0.5 µM 0.135× (z -25.6) |
| [[NCI-H23 (line)]] | alt | 236 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0622× (z -41.5) |
| [[A549 (line)]] | wt | 108 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.108× (z -24.0) |
| [[A-172 (line)]] | wt | 82.3 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.0715× (z -30.0) |
| [[CHP-212 (line)]] | wt | 128 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0969× (z -14.8) |
| [[NCI-H460 (line)]] | wt | 20.6 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.185× (z -15.0) |
| [[CFPAC-1 (line)]] | alt | 36.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -12.8) |
| [[hTERT-HPNE (line)]] | wt | 52.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -15.0) |
| [[NCI-H1792 (line)]] | alt | 31.5 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.127× (z -16.3) |
| [[NCI-H2030 (line)]] | alt | 20.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.240× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 29.5 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.191× (z -12.6) |
| [[H4 (line)]] | wt | 30.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0891× (z -13.9) |
| [[HOP62 (line)]] | alt | 11.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.170× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 22.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -12.4) |
| [[J82 (line)]] | alt | 13.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 12.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.107× (z -12.7) |
| [[A498 (line)]] | wt | 3.98 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.10 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.74 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.19 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.97 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.27 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.56 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8233), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPL]] | +0.67 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[ANKRD18B]] | +0.66 | +0.55 / +0.36 | both halves | 9e-05 |  |
| [[CACNA2D1]] | +0.65 | +0.63 / +0.37 | both halves | 9e-05 |  |
| [[PAXIP1]] | +0.63 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[ZNF101]] | +0.62 | +0.56 / +0.36 | both halves | 1e-04 |  |
| [[DNAJB14]] | +0.62 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[PNISR-AS1]] | +0.62 | +0.41 / +0.30 | both halves | 2e-04 |  |
| [[ZNF253]] | +0.62 | +0.42 / +0.35 | both halves | 1e-04 |  |
| [[ZBTB2]] | +0.62 | +0.39 / +0.42 | both halves | 5e-05 |  |
| [[GABPB1]] | +0.62 | +0.30 / +0.44 | both halves | 2e-04 |  |
| [[ZBED5]] | +0.61 | +0.54 / +0.21 | both halves | 6e-04 |  |
| [[GGPS1]] | +0.61 | +0.48 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL6]] | -0.61 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[WASF3]] | -0.60 | -0.52 / -0.29 | both halves | 3e-04 |  |
| [[STX7]] | -0.60 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[YIF1B]] | -0.58 | -0.37 / -0.23 | both halves | 5e-04 |  |
| [[RIMS3]] | -0.58 | -0.40 / -0.37 | both halves | 9e-05 |  |
| [[PDZD7]] | -0.57 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[PEDS1]] | -0.57 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[CAMK2G]] | -0.57 | -0.38 / -0.35 | both halves | 1e-04 | pathway: MAPK family signaling cascades |
| [[MPP1]] | -0.57 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[SGSM1]] | -0.57 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[HERPUD1]] | -0.56 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[OSBPL9]] | -0.56 | -0.45 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOCS2-AS1]] | B | SOCS2-AS1 activity raises IGF2BP1's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 4.37× lower at baseline in the lines without SOCS2-AS1 | 0.020 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises IGF2BP1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises IGF2BP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT7-DT]] | B | IGF2BP1 activity raises GALNT7-DT's level | lines that do not express IGF2BP1 (23) vs lines expressing it (27) | 1.47× lower at baseline in the lines without IGF2BP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SLFN11, RUNX3, DPY19L2 |
| [[SOCS2-AS1]] | B | IGF2BP1 activity raises SOCS2-AS1's level | lines that do not express IGF2BP1 (23) vs lines expressing it (27) | 2.16× lower at baseline in the lines without IGF2BP1 | 0.013 | ⚠ within organs, on part of the lines; also absent: SLFN11, RUNX3, DPY19L2 |
| [[PBLD]] | B | IGF2BP1 activity raises PBLD's level | lines that do not express IGF2BP1 (23) vs lines expressing it (27) | 1.24× lower at baseline in the lines without IGF2BP1 | 0.030 | ⚠ within organs, on part of the lines; also absent: SLFN11, RUNX3, DPY19L2 |
| [[HDGFL3]] | B | IGF2BP1 activity raises HDGFL3's level | lines that do not express IGF2BP1 (23) vs lines expressing it (27) | 2.64× lower at baseline in the lines without IGF2BP1 | 0.064 | ⚠ within organs, on part of the lines; also absent: SLFN11, RUNX3, DPY19L2 |
| [[STARD4-AS1]] | B | IGF2BP1 activity raises STARD4-AS1's level | lines that do not express IGF2BP1 (23) vs lines expressing it (27) | 1.71× lower at baseline in the lines without IGF2BP1 | 0.069 | ⚠ within organs, on part of the lines; also absent: SLFN11, RUNX3, DPY19L2 |
| [[WASF3]] | C | IGF2BP1 activity raises WASF3's level | lines that do not express IGF2BP1 (23) vs lines expressing it (27) | 3.40× lower at baseline in the lines without IGF2BP1 | 0.016 | ⚠ within organs, on part of the lines; also absent: SLFN11, RUNX3, DPY19L2; co-absent with the target |

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.680). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (4.7, 11.0); signed map (20.3, -22.4). **Vector** length 76.3, 19.9% of its response variance represented; |z| ≥ 3 in 598 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +19.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +18.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +4.1 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.2 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.2 |
|  | [[Benztropine (mesylate) (drug)]] 0.05 µM |  | +1.3 | +1.1 |
|  | [[Vitamin K4 (drug)]] 0.05 µM |  | +1.2 | +2.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.0 | +1.2 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -4.6 | -34.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.5 | -31.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.4 | -27.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.2 | -13.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -7.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -8.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -5.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | insulin like growth factor 2 mRNA binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:48,997,385-49,056,145 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IMP-1, IMP1 |
| Gene groups (HGNC) | RNA binding motif containing |
| Reactome | 4 pathways, smallest: Insulin-like Growth Factor-2 mRNA Binding Proteins (IGF2BPs/IMPs/VICKZs) bind RNA; MAPK6/MAPK4 signaling; MAPK family signaling cascades |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZI8](https://www.uniprot.org/uniprotkb/Q9NZI8) (Insulin-like growth factor 2 mRNA-binding protein 1):

> RNA-binding factor that recruits target transcripts to cytoplasmic protein-RNA complexes (mRNPs). This transcript 'caging' into mRNPs allows mRNA transport and transient storage. It also modulates the rate and location at which target transcripts encounter the translational apparatus and shields them from endonuclease attacks or microRNA-mediated degradation. Preferentially binds to N6-methyladenosine (m6A)-containing mRNAs and increases their stability. Plays a direct role in the transport and …

**Summary**, from NCBI Gene [10642](https://www.ncbi.nlm.nih.gov/gene/10642):

> This gene encodes a member of the insulin-like growth factor 2 mRNA-binding protein family. The protein encoded by this gene contains four K homology domains and two RNA recognition motifs. It functions by binding to the mRNAs of certain genes, including insulin-like growth factor 2, beta-actin and beta-transducin repeat-containing protein, and regulating their translation. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2009]

**Accessions** — [HGNC:28866](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28866) · Entrez [10642](https://www.ncbi.nlm.nih.gov/gene/10642) · UniProt [Q9NZI8](https://www.uniprot.org/uniprotkb/Q9NZI8) · Ensembl [ENSG00000159217](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159217)

## Data

Gene col 8233: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8233); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8233, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8233]; `tensor/DDL_lfc|DDL_z.npy` [8233]; `embed/gene_vectors.npy` [8233]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8233 or target_col == 8233). Every well: [[IGF2BP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGF2BP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
