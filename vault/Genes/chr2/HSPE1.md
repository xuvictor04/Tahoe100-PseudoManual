---
symbol: "HSPE1"
type: "gene"
col: 3693
ensembl_id: "ENSG00000115541"
name: "heat shock protein family E (Hsp10) member 1"
location: "2q33.1"
module: 60
arm: "+"
pooled_cpm: 67.15
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# HSPE1

*heat shock protein family E (Hsp10) member 1* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 7.00× (z +15.5, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.635× (z -5.1, q 2e-04, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (C-33 A 0.182×, BT-474 0.317×, RKO 0.284×, SW480 0.314×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.197×); [[Harringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.136×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CACYBP]] (+0.79, fdr 7e-06), [[HSP90AA2P]] (+0.77, fdr 7e-06), [[HSP90AA1]] (+0.73, fdr 7e-06); moves opposite to [[DOP1A]] (-0.59, fdr 1e-05), [[METTL25B]] (-0.57, fdr 3e-05), [[HARBI1]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3693.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **7.00×** | +15.5 | 0e+00 | 48/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **5.26×** | +13.2 | 3e-37 | 48/48 (SW1417, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **5.16×** | +13.0 | 1e-36 | 48/48 (HT-29, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **3.86×** | +10.7 | 1e-24 | 48/48 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.52×** | +9.4 | 4e-19 | 48/48 (CFPAC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **3.32×** | +9.2 | 4e-18 | 40/43 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **2.56×** | +7.2 | 5e-11 | 45/47 (SHP-77, C32, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **4.95×** | +6.6 | 2e-09 | 40/43 (SW1417, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.39×** | +6.4 | 9e-09 | 36/45 (A549, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM |  | **3.35×** | +5.0 | 3e-05 | 42/47 (A-172, A549, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.85×** | +4.9 | 6e-05 | 42/47 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.80×** | +4.7 | 1e-04 | 39/47 (SW1417, LOX-IMVI, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.44×** | +4.1 | 0.002 | 40/48 (AsPC-1, NCI-H661, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.75×** | +3.6 | 0.013 | 32/49 (HT-29, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 5 µM |  | **2.36×** | +3.6 | 0.014 | 34/48 (HOP62, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.11×** | +3.1 | 0.053 | 32/48 (MIA PaCa-2, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.49×** | +3.0 | 0.066 | 27/47 (BT-474, NCI-H2030, …) | top dose only |  |
| [[Ritonavir (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.075 | 29/48 (RPMI-7951, PANC-1, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.47×** | +2.9 | 0.083 | 31/48 (A498, SW1417, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.46×** | +2.9 | 0.094 | 23/48 (NCI-H1792, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3693.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (C-33 A 0.182×, BT-474 0.317×, RKO 0.284×, SW480 0.314×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.197×); [[Harringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.136×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.635×** | -5.1 | 2e-04 | 31/48 (C-33 A, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.649× | -3.4 | 0.11 | 25/48 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.601× | -3.4 | 0.11 | 30/50 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.447× | -3.4 | 0.11 | 32/49 (BT-474, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.461× | -3.2 | 0.14 | 32/49 (SHP-77, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 0.469× | -3.2 | 0.15 | 31/50 (BT-474, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3693. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 105 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.40× (z +13.0) | — |
| [[A549 (line)]] | wt | 42.1 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.9× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 8.04× (z +11.7) | — |
| [[CFPAC-1 (line)]] | alt | 43.1 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 10.3× (z +14.3) | — |
| [[HOP62 (line)]] | alt | 38.0 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 18.6× (z +16.2) | — |
| [[NCI-H1573 (line)]] | alt | 38.4 | 6 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.87× (z +10.6) | — |
| [[HT-29 (line)]] | alt | 63.2 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 13.5× (z +15.5) | — |
| [[LOX-IMVI (line)]] | wt | 39.1 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 14.8× (z +14.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 64.1 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 13.0× (z +15.3) | — |
| [[NCI-H2347 (line)]] | alt | 57.8 | 4 | 1 | [[Ixazomib citrate (drug)]] 5 µM 5.17× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -8.5) |
| [[SNU-423 (line)]] | alt | 29.8 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 20.2× (z +15.9) | — |
| [[SW480 (line)]] | alt | 88.8 | 4 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 10.3× (z +13.7) | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -9.6) |
| [[A-172 (line)]] | wt | 51.5 | 4 | 0 | [[Auranofin (drug)]] 5 µM 11.1× (z +14.2) | — |
| [[BT-474 (line)]] | alt | 70.5 | 3 | 1 | [[Auranofin (drug)]] 5 µM 9.98× (z +15.4) | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -10.9) |
| [[C32 (line)]] | wt | 35.3 | 4 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 16.4× (z +15.0) | — |
| [[COLO 205 (line)]] | alt | 31.6 | 4 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 11.0× (z +9.9) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 7.88× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 41.6 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 9.14× (z +13.4) | — |
| [[hTERT-HPNE (line)]] | wt | 29.7 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 11.8× (z +10.9) | — |
| [[J82 (line)]] | alt | 85.2 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.20× (z +11.5) | — |
| [[KATO III (line)]] | alt | 95.3 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.68× (z +12.4) | — |
| [[Panc 03.27 (line)]] | alt | 40.8 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.18× (z +12.5) | — |
| [[RKO (line)]] | wt | 93.9 | 3 | 1 | [[Auranofin (drug)]] 5 µM 8.60× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -9.8) |
| [[SW1417 (line)]] | alt | 92.6 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.38× (z +15.8) | — |
| [[A-427 (line)]] | wt | 135 | 1 | 2 | [[Auranofin (drug)]] 5 µM 6.24× (z +10.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 57.3 | 3 | 0 | [[Auranofin (drug)]] 5 µM 8.43× (z +12.9) | — |
| [[Hs 766T (line)]] | wt | 45.6 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.79× (z +10.4) | — |
| [[LoVo (line)]] | wt | 94.2 | 3 | 0 | [[Auranofin (drug)]] 5 µM 6.19× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 79.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.95× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.06× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 58.6 | 3 | 0 | [[Auranofin (drug)]] 5 µM 9.16× (z +13.0) | — |
| [[SW 900 (line)]] | alt | 53.6 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.17× (z +12.2) | — |
| [[AN3 CA (line)]] | alt | 58.7 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 8.61× (z +9.8) | [[Harringtonine (drug)]] 5 µM 0.136× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 57.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.54× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 95.5 | 1 | 1 | [[Auranofin (drug)]] 5 µM 6.84× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 27.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.3× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H23 (line)]] | alt | 95.3 | 1 | 1 | [[Auranofin (drug)]] 5 µM 4.64× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -9.6) |
| [[PANC-1 (line)]] | alt | 80.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[SHP-77 (line)]] | alt | 74.2 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 8.85× (z +13.7) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.51× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 50.9 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 10.2× (z +12.9) | — |
| [[SNU-1 (line)]] | wt | 63.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 10.5× (z +13.3) | — |
| [[H4 (line)]] | wt | 48.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 11.0× (z +11.4) | — |
| [[HepG2_C3A (line)]] | wt | 89.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.31× (z +9.7) | — |
| [[CHP-212 (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 90.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 82.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3693), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACYBP]] | +0.79 | +0.79 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 556 |
| [[HSP90AA2P]] | +0.77 | +0.77 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[HSP90AA1]] | +0.73 | +0.72 / +0.76 | both halves | 7e-06 | STRING 942 |
| [[HSPD1]] | +0.72 | +0.76 / +0.70 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MTORC1_SIGNALING; STRING 999; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[AHSA1]] | +0.72 | +0.72 / +0.68 | both halves | 7e-06 | STRING 831 |
| [[CHRNA5]] | +0.69 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[CCT4]] | +0.69 | +0.64 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 893 |
| [[HSPA1B]] | +0.69 | +0.61 / +0.72 | both halves | 7e-06 | pathway: Mitochondrial unfolded protein response (UPRmt); STRING 845 |
| [[PSMA1]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 411 |
| [[TXN]] | +0.68 | +0.61 / +0.67 | both halves | 7e-06 | STRING 810 |
| [[SOD1]] | +0.68 | +0.69 / +0.63 | both halves | 7e-06 | STRING 688 |
| [[CHORDC1]] | +0.68 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[HSP90AB3P]] | +0.67 | +0.63 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOP1A]] | -0.59 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[METTL25B]] | -0.57 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[HARBI1]] | -0.57 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[YY1AP1]] | -0.56 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[NR1D1]] | -0.55 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[FAM161B]] | -0.54 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[CGGBP1]] | -0.54 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[HCFC2]] | -0.54 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[NFKB2]] | -0.53 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[CEP63]] | -0.53 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[TADA3]] | -0.53 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[POLI]] | -0.53 | -0.57 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.820). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.4, -11.0); signed map (-25.8, -28.8). **Vector** length 98.3, 41.9% of its response variance represented; |z| ≥ 3 in 1,008 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Attenuation phase* (reactome, mean cos +0.56 to 13); *HSF1-dependent transactivation* (reactome, mean cos +0.54 to 14); *Cellular response to heat stress* (reactome, mean cos +0.53 to 18).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.5 | +13.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.4 | +9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.2 | +15.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.2 | +13.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +7.9 | +6.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.4 | +3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +0.2 |
|  | [[Infigratinib (drug)]] 5 µM |  | +2.1 | +3.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.6 | -3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | +0.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.8 | -5.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -0.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.3 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.8 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein family E (Hsp10) member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:197,500,140-197,503,449 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CPN10, GroES, HSP10, EPF |
| Gene groups (HGNC) | Chaperonins |
| Hallmark sets | MYC_TARGETS_V2, MTORC1_SIGNALING, MYC_TARGETS_V1 |
| Reactome | 7 pathways, smallest: Mitochondrial unfolded protein response (UPRmt); RHOG GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P61604](https://www.uniprot.org/uniprotkb/P61604) (10 kDa heat shock protein, mitochondrial):

> Co-chaperonin implicated in mitochondrial protein import and macromolecular assembly. Together with Hsp60, facilitates the correct folding of imported proteins. May also prevent misfolding and promote the refolding and proper assembly of unfolded polypeptides generated under stress conditions in the mitochondrial matrix. The functional units of these chaperonins consist of heptameric rings of the large subunit Hsp60, which function as a back-to-back double ring. In a cyclic reaction, Hsp60 ring …

**Summary**, from NCBI Gene [3336](https://www.ncbi.nlm.nih.gov/gene/3336):

> This gene encodes a major heat shock protein which functions as a chaperonin. Its structure consists of a heptameric ring which binds to another heat shock protein in order to form a symmetric, functional heterodimer which enhances protein folding in an ATP-dependent manner. This gene and its co-chaperonin, HSPD1, are arranged in a head-to-head orientation on chromosome 2. Naturally occurring read-through transcription occurs between this locus and the neighboring locus MOBKL3.[provided by …

**Accessions** — [HGNC:5269](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5269) · Entrez [3336](https://www.ncbi.nlm.nih.gov/gene/3336) · UniProt [P61604](https://www.uniprot.org/uniprotkb/P61604) · Ensembl [ENSG00000115541](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115541)

## Data

Gene col 3693: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3693); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3693, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3693]; `tensor/DDL_lfc|DDL_z.npy` [3693]; `embed/gene_vectors.npy` [3693]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3693 or target_col == 3693). Every well: [[HSPE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSPE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
