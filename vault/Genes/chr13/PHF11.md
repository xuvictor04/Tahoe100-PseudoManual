---
symbol: "PHF11"
type: "gene"
col: 5821
ensembl_id: "ENSG00000136147"
name: "PHD finger protein 11"
location: "13q14.2"
module: 32
arm: "+"
pooled_cpm: 25.29
n_lines_expressing: 47
n_dd_up: 19
n_dd_down: 35
n_dd_up_clean: 16
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 30
direction_downstream: 50
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# PHF11

*PHD finger protein 11* — 13q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.58× (z +7.5, q 3e-11, up in 33 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (10 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.186× (z -28.5, q 0e+00, down in 44 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NMI]] (+0.89, fdr 7e-06), [[PARP14]] (+0.87, fdr 7e-06), [[DTX3L]] (+0.86, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[MX1]] → it (grade B ⚠); 50 go from it, the strongest it → cells under [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5821.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.58×** | +7.5 | 3e-11 | 33/44 (SW1417, Hs 766T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +5.2 | 5e-05 | 22/45 (KATO III, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +5.2 | 5e-05 | 18/44 (NCI-H2347, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +5.0 | 5e-05 | 20/44 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +5.0 | 5e-05 | 18/44 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.36×** | +5.0 | 5e-05 | 21/44 (SW480, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.22×** | +4.6 | 3e-04 | 16/45 (SW480, LOX-IMVI, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.28×** | +4.4 | 7e-04 | 16/45 (SW480, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.002 | 15/45 (Hs 766T, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.27×** | +4.0 | 0.003 | 14/45 (Hs 766T, RKO, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.21×** | +4.0 | 0.003 | 12/45 (SW480, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | 1.17× | +3.8 | 0.007 | 12/45 (A-172, COLO 205, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.008 | 14/45 (Hs 766T, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.013 | 13/44 (KATO III, COLO 205, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.24×** | +3.5 | 0.020 | 14/43 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.16× | +3.4 | 0.021 | 10/45 (SW480, AsPC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5821.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.186×** | -28.5 | 0e+00 | 44/45 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.191×** | -28.1 | 0e+00 | 44/45 (COLO 205, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.241×** | -24.2 | 0e+00 | 43/45 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.367×** | -17.0 | 0e+00 | 41/43 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.385×** | -16.2 | 0e+00 | 42/45 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.469×** | -12.8 | 9e-36 | 37/45 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.606×** | -12.0 | 2e-31 | 30/45 (MIA PaCa-2, COLO 205, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.497×** | -11.9 | 1e-30 | 35/43 (NCI-H2030, SW480, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.662×** | -9.9 | 3e-21 | 29/45 (LoVo, COLO 205, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.564×** | -9.7 | 2e-20 | 34/45 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.565×** | -9.7 | 2e-20 | 34/45 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.344×** | -9.5 | 1e-19 | 37/45 (SNU-423, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.588×** | -9.0 | 1e-17 | 29/45 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.590×** | -9.0 | 1e-17 | 32/45 (SW480, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.597×** | -8.8 | 7e-17 | 31/44 (HCT15, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.710×** | -8.2 | 7e-15 | 30/45 (A-172, SNU-423, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.436×** | -7.4 | 6e-12 | 29/45 (A549, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.656×** | -7.1 | 3e-11 | 27/45 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.470×** | -6.7 | 6e-10 | 28/43 (HS-578T, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5821. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 35.2 | 0 | 14 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.116× (z -18.4) |
| [[SNU-423 (line)]] | alt | 44.7 | 0 | 12 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0765× (z -22.4) |
| [[A549 (line)]] | wt | 34.8 | 0 | 9 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0767× (z -18.1) |
| [[A-172 (line)]] | wt | 54.8 | 0 | 8 | — | [[Belinostat (drug)]] 5 µM 0.101× (z -21.1) |
| [[NCI-H23 (line)]] | alt | 36.3 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.105× (z -17.3) |
| [[RKO (line)]] | wt | 33.3 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -12.8) |
| [[SW480 (line)]] | alt | 22.9 | 0 | 8 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.138× (z -18.4) |
| [[COLO 205 (line)]] | alt | 177 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -22.1) |
| [[MIA PaCa-2 (line)]] | alt | 34.0 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.0706× (z -18.5) |
| [[NCI-H460 (line)]] | wt | 14.9 | 1 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[Belinostat (drug)]] 5 µM 0.130× (z -16.2) |
| [[PANC-1 (line)]] | alt | 23.3 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.237× (z -15.2) |
| [[RPMI-7951 (line)]] | alt | 47.5 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.103× (z -17.3) |
| [[A498 (line)]] | wt | 26.6 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.193× (z -15.0) |
| [[AsPC-1 (line)]] | alt | 21.5 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.166× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 18.5 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.181× (z -13.5) |
| [[HS-578T (line)]] | alt | 26.2 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.141× (z -13.2) |
| [[BT-474 (line)]] | alt | 24.3 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.182× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 25.2 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.227× (z -12.0) |
| [[J82 (line)]] | alt | 31.3 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.210× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 19.1 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.151× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 24.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0700× (z -20.1) |
| [[NCI-H1792 (line)]] | alt | 22.3 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.102× (z -14.7) |
| [[Panc 03.27 (line)]] | alt | 52.7 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.176× (z -16.3) |
| [[HepG2_C3A (line)]] | wt | 29.4 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.159× (z -10.7) |
| [[Hs 766T (line)]] | wt | 38.1 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.166× (z -13.3) |
| [[KATO III (line)]] | alt | 17.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -12.8) |
| [[NCI-H2347 (line)]] | alt | 23.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -10.7) |
| [[H4 (line)]] | wt | 18.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0819× (z -11.8) |
| [[hTERT-HPNE (line)]] | wt | 21.6 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.193× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 10.00 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0694× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.161× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 20.2 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.127× (z -11.6) |
| [[SW 900 (line)]] | alt | 19.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0546× (z -8.8) |
| [[SW1417 (line)]] | alt | 12.5 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.113× (z -11.8) |
| [[A-427 (line)]] | wt | 13.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.186× (z -9.8) |
| [[HCT15 (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.162× (z -8.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HT-29 (line)]] | alt | 12.3 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.161× (z -10.5) |
| [[SW48 (line)]] | wt | 9.69 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0595× (z -9.1) |
| [[AN3 CA (line)]] | alt | 4.33 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5821), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NMI]] | +0.89 | +0.85 / +0.89 | both halves | 7e-06 | STRING 570 |
| [[PARP14]] | +0.87 | +0.80 / +0.87 | both halves | 7e-06 |  |
| [[DTX3L]] | +0.86 | +0.76 / +0.88 | both halves | 7e-06 |  |
| [[DDX60L]] | +0.85 | +0.73 / +0.87 | both halves | 7e-06 |  |
| [[IFIT5]] | +0.85 | +0.77 / +0.84 | both halves | 7e-06 | STRING 405 |
| [[HERC6]] | +0.83 | +0.73 / +0.86 | both halves | 7e-06 |  |
| [[PARP10]] | +0.83 | +0.70 / +0.85 | both halves | 7e-06 |  |
| [[TRIM21]] | +0.82 | +0.71 / +0.83 | both halves | 7e-06 |  |
| [[PARP12]] | +0.82 | +0.65 / +0.90 | both halves | 7e-06 |  |
| [[PARP9]] | +0.81 | +0.66 / +0.88 | both halves | 7e-06 | STRING 451 |
| [[SAMD9L]] | +0.81 | +0.67 / +0.87 | both halves | 7e-06 | STRING 433 |
| [[DDX60]] | +0.81 | +0.73 / +0.82 | both halves | 7e-06 | STRING 417 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 11, C 19. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MX1]] | B | MX1 activity raises PHF11's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.98× lower at baseline in the lines without MX1 | 0.008 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[OAS2]] | B | OAS2 activity strengthens PHF11's drug response | lines that do not express OAS2 (12) vs lines expressing it (33) | the lines without OAS2 respond 0.72× as strongly (z diff +1.00); strongest at Fedratinib (hydrochloride hydrate) 5 µM: 0.70x vs 0.43x (z diff +3.1) | 0.014 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1; target measured in part of the lines; artifact flags |
| [[GBP4]] | B | GBP4 activity raises PHF11's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.08× lower at baseline in the lines without GBP4 | 0.018 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[EPSTI1]] | B | EPSTI1 activity raises PHF11's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 1.95× lower at baseline in the lines without EPSTI1 | 0.048 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[OASL]] | B | OASL activity raises PHF11's level | lines that do not express OASL (10) vs lines expressing it (40) | 2.25× lower at baseline in the lines without OASL | 0.054 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers PHF11's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[GSDMD]] | B | GSDMD activity raises PHF11's level | lines that do not express GSDMD (7) vs lines expressing it (43) | 2.77× lower at baseline in the lines without GSDMD | 0.074 | ⚠ within organs, on part of the lines; co-absent genes; also absent: TGFBR2, VDR, IL1RAP |
| [[GBP1]] | B | GBP1 activity raises PHF11's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 1.90× lower at baseline in the lines without GBP1 | 0.074 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[IFI6]] | B | IFI6 activity strengthens PHF11's drug response | lines that do not express IFI6 (12) vs lines expressing it (33) | the lines without IFI6 respond 0.67× as strongly (z diff +1.43); strongest at Fedratinib (hydrochloride hydrate) 5 µM: 0.64x vs 0.44x (z diff +2.8) | 0.079 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[IFI16]] | B | IFI16 activity raises PHF11's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 1.51× lower at baseline in the lines without IFI16 | 0.090 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[JAK2]] | B | JAK2 activity raises PHF11's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 7.0% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[SP100]] | C | SP100's natural level strengthens PHF11's drug response | SP100's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.80, reverse +0.41; direction clear | 0.002 | ⚠ tissue can mimic it; precision caveat |

### Downstream of this gene

*50 arrows, 50 of them with an alert ⚠; grade A 0, B 0, C 50. Shown: the 12 strongest; 38 more arrows (38 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM | C | PHF11 activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express PHF11 (3) vs lines expressing it (45) | the lines without PHF11: 0.68× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | C | PHF11 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express PHF11 (3) vs lines expressing it (45) | the lines without PHF11: 0.68× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| cells under [[AT7519 (drug)]] 5 µM | C | PHF11 activity raises the cells' numbers under AT7519 5 µM (protects the cells) | lines that do not express PHF11 (3) vs lines expressing it (45) | the lines without PHF11: 0.41× the cells of the other lines | 0.008 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| cells under [[Sulfatinib (drug)]] 5 µM | C | PHF11 activity raises the cells' numbers under Sulfatinib 5 µM (protects the cells) | lines that do not express PHF11 (3) vs lines expressing it (45) | the lines without PHF11: 0.64× the cells of the other lines | 0.008 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| cells under [[Tucatinib (drug)]] 5 µM | C | PHF11 activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express PHF11 (3) vs lines expressing it (45) | the lines without PHF11: 0.64× the cells of the other lines | 0.008 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| cells under [[Entecavir (monohydrate) (drug)]] 0.5 µM | C | PHF11 activity raises the cells' numbers under Entecavir (monohydrate) 0.5 µM (protects the cells) | lines that do not express PHF11 (3) vs lines expressing it (45) | the lines without PHF11: 0.65× the cells of the other lines | 0.008 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | PHF11 activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express PHF11 (3) vs lines expressing it (45) | the lines without PHF11: 0.72× the cells of the other lines | 0.008 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| cells under [[Entrectinib (drug)]] 5 µM | C | PHF11 activity lowers the cells' numbers under Entrectinib 5 µM (makes them more sensitive) | lines that do not express PHF11 (3) vs lines expressing it (45) | the lines without PHF11: 1.37× the cells of the other lines | 0.010 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| cells under [[Tranilast (drug)]] 0.5 µM | C | PHF11 activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express PHF11 (3) vs lines expressing it (45) | the lines without PHF11: 0.72× the cells of the other lines | 0.011 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| [[IFIH1]] | C | PHF11 activity raises IFIH1's level | lines that do not express PHF11 (3) vs lines expressing it (47) | 3.58× lower at baseline in the lines without PHF11 | 0.011 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| cells under [[Tirabrutinib (drug)]] 0.5 µM | C | PHF11 activity lowers the cells' numbers under Tirabrutinib 0.5 µM (makes them more sensitive) | lines that do not express PHF11 (3) vs lines expressing it (45) | the lines without PHF11: 1.38× the cells of the other lines | 0.012 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| [[GSDMD]] | C | PHF11 activity raises GSDMD's level | lines that do not express PHF11 (3) vs lines expressing it (47) | 4.44× lower at baseline in the lines without PHF11 | 0.014 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.840). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.5, 53.9); signed map (62.7, 32.1). **Vector** length 116, 34.8% of its response variance represented; |z| ≥ 3 in 1,366 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.68 to 56); *interferon gamma response* (hallmark, mean cos +0.69 to 60); *interferon* (control, mean cos +0.73 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.5 | +5.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.4 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.4 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +6.2 | +5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.1 | -4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.8 | +7.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.6 | +5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +3.8 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -7.0 | -17.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -6.8 | -12.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -5.9 | -7.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -5.9 | -9.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.8 | -16.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -5.7 | -9.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -5.0 | -12.8 |

## What is on record

|  |  |
|---|---|
| Name | PHD finger protein 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.2 — chr13:49,495,610-49,528,981 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NY-REN-34, BCAP, IGER |
| Gene groups (HGNC) | PHD finger proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UIL8](https://www.uniprot.org/uniprotkb/Q9UIL8) (PHD finger protein 11):

> Positive regulator of Th1-type cytokine gene expression.

**Summary**, from NCBI Gene [51131](https://www.ncbi.nlm.nih.gov/gene/51131):

> This gene encodes a protein containing a PHD (plant homeodomain) type zinc finger. This gene has been identified in some studies as a candidate gene for asthma. Naturally-occurring readthrough transcription may occur from the upstream SETDB2 (SET domain bifurcated 2) gene to this locus. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:17024](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17024) · Entrez [51131](https://www.ncbi.nlm.nih.gov/gene/51131) · UniProt [Q9UIL8](https://www.uniprot.org/uniprotkb/Q9UIL8) · Ensembl [ENSG00000136147](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136147)

## Data

Gene col 5821: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5821); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5821, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5821]; `tensor/DDL_lfc|DDL_z.npy` [5821]; `embed/gene_vectors.npy` [5821]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5821 or target_col == 5821). Every well: [[PHF11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHF11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
