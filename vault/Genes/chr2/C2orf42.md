---
symbol: "C2orf42"
type: "gene"
col: 3748
ensembl_id: "ENSG00000115998"
name: "chromosome 2 open reading frame 42"
location: "2p13.3"
module: 46
arm: "+"
pooled_cpm: 83.62
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 13
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# C2orf42

*chromosome 2 open reading frame 42* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +7.8, q 3e-12, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.347× (z -18.2, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.506× (z -12.2, q 5e-32, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAPPC13]] (+0.75, fdr 7e-06), [[TSTD3]] (+0.70, fdr 2e-05), [[NMNAT1]] (+0.69, fdr 1e-05); moves opposite to [[EDA]] (-0.60, fdr 5e-05), [[ATP1A3]] (-0.59, fdr 1e-04), [[TPPP]] (-0.58, fdr 5e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ATAD2B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3748.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +7.8 | 3e-12 | 41/48 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.8 | 2e-06 | 28/49 (AsPC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +4.0 | 0.011 | 28/47 (NCI-H1573, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.011 | 24/48 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.24×** | +3.9 | 0.011 | 22/49 (A549, RKO, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.015 | 23/47 (AsPC-1, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.065 | 24/49 (SW480, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3748.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.347×** | -18.2 | 0e+00 | 43/44 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.371×** | -17.7 | 0e+00 | 46/49 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.453×** | -13.1 | 6e-37 | 39/45 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.506×** | -12.2 | 5e-32 | 47/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.507×** | -12.1 | 8e-32 | 48/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.565×** | -10.2 | 2e-22 | 47/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.695×** | -6.5 | 7e-09 | 41/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.693×** | -6.3 | 2e-08 | 35/47 (SHP-77, C32, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.737×** | -5.4 | 4e-06 | 34/48 (C-33 A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.753×** | -5.0 | 3e-05 | 28/48 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.762×** | -4.8 | 7e-05 | 34/48 (AN3 CA, A549, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.937× | -4.0 | 0.003 | 1/50 (NCI-H2122) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.822×** | -3.5 | 0.022 | 20/48 (SW 900, SW480, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.818×** | -3.4 | 0.025 | 22/47 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.865× | -3.0 | 0.091 | 19/48 (C32, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3748. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 152 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.364× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 104 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.367× (z -12.7) |
| [[LOX-IMVI (line)]] | wt | 89.8 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.363× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 101 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.343× (z -11.6) |
| [[PANC-1 (line)]] | alt | 93.4 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.426× (z -10.7) |
| [[SW480 (line)]] | alt | 108 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.496× (z -9.9) |
| [[A-172 (line)]] | wt | 96.4 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -18.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 104 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.334× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 81.4 | 2 | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.304× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 94.4 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.334× (z -13.3) |
| [[NCI-H23 (line)]] | alt | 122 | 1 | 4 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.117× (z -24.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.476× (z -8.8) |
| [[A-427 (line)]] | wt | 129 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -24.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.448× (z -9.7) |
| [[HOP62 (line)]] | alt | 84.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.438× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 102 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.393× (z -11.0) |
| [[A498 (line)]] | wt | 82.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -19.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 116 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0615× (z -18.9) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 71.4 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -12.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 70.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -23.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 58.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -12.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 73.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -13.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 79.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -11.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 81.9 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.273× (z -13.9) ⚠ toxic |
| [[A549 (line)]] | wt | 94.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -15.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 68.1 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.325× (z -10.8) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.403× (z -9.1) |
| [[CHP-212 (line)]] | wt | 97.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -12.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 61.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -13.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 88.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 56.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.454× (z -8.9) |
| [[SW 900 (line)]] | alt | 90.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -13.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 88.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -17.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 61.8 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.274× (z -10.8) |
| [[HCT15 (line)]] | alt | 78.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -11.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 64.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 74.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0826× (z -10.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 70.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -13.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 86.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -20.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 83.1 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.113× (z -9.7) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 91.0 | 0 | 1 | — | [[Fenofibrate (drug)]] 5 µM 0.100× (z -8.5) |
| [[BT-474 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 88.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 74.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 70.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3748), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC13]] | +0.75 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[TSTD3]] | +0.70 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[NMNAT1]] | +0.69 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[ATAD2B]] | +0.67 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[MTG2]] | +0.66 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[ACOT2]] | +0.66 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[DDX59]] | +0.65 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[RAF1]] | +0.65 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[ZNF785]] | +0.65 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[ZBTB8OS]] | +0.64 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[SEC24B-AS1]] | +0.64 | +0.54 / +0.36 | both halves | 9e-05 |  |
| [[SUZ12P1]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDA]] | -0.60 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[ATP1A3]] | -0.59 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[TPPP]] | -0.58 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[FCHO1]] | -0.55 | -0.39 / -0.18 | ⚠ not reproduced | 0.001 |  |
| [[CAST]] | -0.55 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[CORO1C]] | -0.55 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[ACTG1]] | -0.55 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[FLNB]] | -0.54 | -0.44 / -0.25 | both halves | 4e-04 |  |
| [[OSBPL8]] | -0.54 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[TTLL12]] | -0.54 | -0.44 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers C2orf42's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers C2orf42's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[KIF1A]] | B | KIF1A activity raises C2orf42's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 1.27× lower at baseline in the lines without KIF1A | 0.087 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[ZNF785]] | B | ZNF785 activity lowers C2orf42's level | lines that do not express ZNF785 (9) vs lines expressing it (41) | 1.33× higher at baseline in the lines without ZNF785 | 0.093 | ⚠ within organs, on part of the lines; also absent: TNFRSF14, BDH1, PARP8 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATAD2B]] | C | C2orf42's natural level strengthens ATAD2B's drug response | C2orf42's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.44; direction not clear | 0.051 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.721). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-5.6, 16.0); signed map (25.0, -14.9). **Vector** length 119, 37.1% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +10.2 | +4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.2 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +5.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.7 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.9 | +2.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.5 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +3.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.9 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.7 | +1.8 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -7.4 | -12.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.1 | -10.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.8 | -12.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.0 | -6.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.8 | -5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | -2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.9 | -3.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.3 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 2 open reading frame 42 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:70,149,885-70,248,615 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20558 |
| Matched by | ensembl_id |

UniProt [Q9NWW7](https://www.uniprot.org/uniprotkb/Q9NWW7) carries no function annotation.

**Summary**, from NCBI Gene [54980](https://www.ncbi.nlm.nih.gov/gene/54980):

> Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26056](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26056) · Entrez [54980](https://www.ncbi.nlm.nih.gov/gene/54980) · UniProt [Q9NWW7](https://www.uniprot.org/uniprotkb/Q9NWW7) · Ensembl [ENSG00000115998](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115998)

## Data

Gene col 3748: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3748); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3748, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3748]; `tensor/DDL_lfc|DDL_z.npy` [3748]; `embed/gene_vectors.npy` [3748]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3748 or target_col == 3748). Every well: [[C2orf42 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C2orf42.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
