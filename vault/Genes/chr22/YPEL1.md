---
symbol: "YPEL1"
type: "gene"
col: 1845
ensembl_id: "ENSG00000100027"
name: "yippee like 1"
location: "22q11.21-q11.22"
module: 22
arm: "+"
pooled_cpm: 20.11
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 37
n_dd_up_clean: 12
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# YPEL1

*yippee like 1* — 22q11.21-q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.99× (z +13.8, q 3e-40, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (10 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.237× (z -20.3, q 0e+00, down in 46 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.332× (z -15.6, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL6IP1]] (+0.66, fdr 7e-06), [[CDC25C]] (+0.61, fdr 1e-05), [[AAMDC]] (+0.60, fdr 1e-05); moves opposite to [[TRIM16]] (-0.53, fdr 4e-05), [[KCTD14]] (-0.49, fdr 6e-05), [[SLC10A7]] (-0.49, fdr 8e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1845.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +13.8 | 3e-40 | 34/46 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.94×** | +9.4 | 1e-18 | 31/47 (A498, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +9.3 | 3e-18 | 32/46 (A498, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.79×** | +8.2 | 3e-14 | 26/47 (A498, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.86×** | +4.6 | 5e-04 | 18/46 (HOP62, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.36×** | +4.4 | 1e-03 | 15/47 (KATO III, SNU-423, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.2 | 0.002 | 22/47 (RKO, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +3.7 | 0.013 | 17/47 (SW1417, HT-29, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.63×** | +3.6 | 0.019 | 12/46 (NCI-H2347, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.30×** | +3.5 | 0.026 | 9/47 (A-427, NCI-H2347, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.57×** | +3.4 | 0.039 | 11/46 (HOP62, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.27×** | +3.3 | 0.054 | 14/46 (A-172, NCI-H2030, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.078 | 5/46 (Hs 766T, PANC-1, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.35×** | +3.0 | 0.096 | 6/47 (PANC-1, Panc 03.27, …) | two highest doses | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.24×** | +3.0 | 0.096 | 6/47 (NCI-H2347, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1845.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.237×** | -20.3 | 0e+00 | 46/46 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.332×** | -15.6 | 0e+00 | 44/47 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.381×** | -13.1 | 7e-37 | 40/47 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.398×** | -13.0 | 2e-36 | 37/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.450×** | -11.3 | 2e-27 | 36/46 (SNU-1, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.503×** | -9.7 | 3e-20 | 32/47 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.503×** | -9.3 | 9e-19 | 16/27 (NCI-H2030, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.290×** | -9.1 | 4e-18 | 35/47 (NCI-H23, A-427, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.519×** | -8.7 | 1e-16 | 32/47 (PANC-1, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.540×** | -8.7 | 2e-16 | 27/47 (PANC-1, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.311×** | -8.6 | 3e-16 | 36/46 (HOP62, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.544×** | -8.6 | 4e-16 | 27/46 (SW 900, NCI-H1792, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.536×** | -8.5 | 1e-15 | 29/45 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.576×** | -7.8 | 3e-13 | 26/47 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.349×** | -7.8 | 3e-13 | 33/47 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.581×** | -7.7 | 6e-13 | 30/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.599×** | -7.2 | 2e-11 | 26/46 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.381×** | -7.1 | 3e-11 | 30/43 (SW 900, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.493×** | -7.1 | 3e-11 | 29/47 (SW480, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.396×** | -6.8 | 2e-10 | 27/46 (SK-MEL-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1845. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 28.1 | 0 | 12 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0823× (z -20.5) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -15.1) |
| [[NCI-H460 (line)]] | wt | 18.7 | 0 | 11 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.109× (z -15.7) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.156× (z -13.2) |
| [[A-427 (line)]] | wt | 35.4 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -16.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -14.5) |
| [[SNU-423 (line)]] | alt | 31.1 | 0 | 9 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0980× (z -14.3) |
| [[SW 900 (line)]] | alt | 28.4 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0828× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.154× (z -11.0) |
| [[A549 (line)]] | wt | 19.8 | 1 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.136× (z -12.7) |
| [[SW480 (line)]] | alt | 21.5 | 0 | 7 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.130× (z -16.4) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.257× (z -11.0) |
| [[HOP62 (line)]] | alt | 23.7 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.153× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 59.3 | 0 | 6 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0409× (z -24.2) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.122× (z -15.3) |
| [[SNU-1 (line)]] | wt | 46.8 | 0 | 6 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.111× (z -12.4) |
| [[C-33 A (line)]] | alt | 89.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.186× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 39.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0521× (z -12.4) |
| [[A-172 (line)]] | wt | 15.7 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +10.4) | [[Harringtonine (drug)]] 0.5 µM 0.0858× (z -14.8) |
| [[A498 (line)]] | wt | 6.13 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.03× (z +13.4) | — |
| [[AN3 CA (line)]] | alt | 52.6 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0872× (z -11.0) |
| [[C32 (line)]] | wt | 27.0 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0731× (z -12.4) ⚠ toxic; cell-cycle shift, explains ~17% of this change |
| [[NCI-H1792 (line)]] | alt | 18.9 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0982× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW1417 (line)]] | alt | 21.9 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.57× (z +9.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.126× (z -13.2) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 21.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.287× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 7.63 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +10.8) | — |
| [[NCI-H2030 (line)]] | alt | 21.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H2347 (line)]] | alt | 20.5 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.174× (z -11.2) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.267× (z -8.5) |
| [[RKO (line)]] | wt | 10.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.190× (z -8.7) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 12.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +8.5) | — |
| [[KATO III (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.137× (z -9.6) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 6.93 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H1573 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SK-MEL-2 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.147× (z -10.4) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 20.7 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0817× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1845), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL6IP1]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[CDC25C]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[AAMDC]] | +0.60 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[CEP68]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[UBALD2]] | +0.57 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[TESK2]] | +0.56 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[PTTG1]] | +0.56 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[STMN1]] | +0.54 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[FBXL20]] | +0.53 | +0.40 / +0.60 | both halves | 5e-05 | STRING 511 |
| [[SUN2]] | +0.53 | +0.39 / +0.53 | both halves | 5e-05 |  |
| [[OSER1-DT]] | +0.52 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[ZBTB44]] | +0.52 | +0.49 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM16]] | -0.53 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[KCTD14]] | -0.49 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[SLC10A7]] | -0.49 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[TOMM40L]] | -0.48 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[BMS1]] | -0.47 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[LARP4]] | -0.47 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[TMEM33]] | -0.47 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[RRP15]] | -0.47 | -0.26 / -0.57 | both halves | 3e-04 |  |
| [[RABGGTB]] | -0.46 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[RRS1]] | -0.46 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[VWA8]] | -0.45 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[AGK]] | -0.45 | -0.39 / -0.48 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers YPEL1's level | compounds that target MTOR: 5 of 8 raise it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.9% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TTC22]] | B | TTC22 activity lowers YPEL1's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 1.73× higher at baseline in the lines without TTC22 | 0.052 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5 |
| [[PIMREG]] | B | PIMREG activity raises YPEL1's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.02× lower at baseline in the lines without PIMREG | 0.057 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.415). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.6, -50.6); signed map (-53.1, -40.0). **Vector** length 98.6, 26.1% of its response variance represented; |z| ≥ 3 in 1,382 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.1 | +3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.0 | +1.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.0 | +3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +13.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | +4.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +1.9 | +2.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.3 | -15.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.7 | -20.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.8 | -8.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.3 | -13.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.0 | -11.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.7 | -6.8 |
|  | [[EX229 (drug)]] 5 µM |  | -4.7 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -7.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.3 | -7.1 |

## What is on record

|  |  |
|---|---|
| Name | yippee like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21-q11.22 — chr22:21,697,536-21,735,794 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Yippee like family |
| Hallmark sets | KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [O60688](https://www.uniprot.org/uniprotkb/O60688) (Protein yippee-like 1):

> May play a role in epithelioid conversion of fibroblasts.

**Summary**, from NCBI Gene [29799](https://www.ncbi.nlm.nih.gov/gene/29799):

> This gene is located in the region associated with DiGeorge syndrome on chromosome 22. The encoded protein localizes to the centrosome and nucleolus and may play a role in the regulation of cell division. [provided by RefSeq, Feb 2015]

**Accessions** — [HGNC:12845](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12845) · Entrez [29799](https://www.ncbi.nlm.nih.gov/gene/29799) · UniProt [O60688](https://www.uniprot.org/uniprotkb/O60688) · Ensembl [ENSG00000100027](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100027)

## Data

Gene col 1845: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1845); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1845, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1845]; `tensor/DDL_lfc|DDL_z.npy` [1845]; `embed/gene_vectors.npy` [1845]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1845 or target_col == 1845). Every well: [[YPEL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YPEL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
