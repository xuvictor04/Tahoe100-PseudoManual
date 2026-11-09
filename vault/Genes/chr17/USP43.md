---
symbol: "USP43"
type: "gene"
col: 7852
ensembl_id: "ENSG00000154914"
name: "ubiquitin specific peptidase 43"
location: "17p13.1"
module: 14
arm: "+"
pooled_cpm: 28.14
n_lines_expressing: 40
n_dd_up: 17
n_dd_down: 11
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 7
direction_downstream: 7
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# USP43

*ubiquitin specific peptidase 43* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.89× (z +31.2, q 0e+00, up in 30 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.568× (z -11.3, q 9e-27, down in 20 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.638× (z -9.3, q 3e-18, down in 22 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC2A6]] (+0.61, fdr 1e-05), [[PLEKHG3]] (+0.59, fdr 2e-05), [[S100A3]] (+0.57, fdr 2e-05); moves opposite to [[DNAJC24]] (-0.56, fdr 2e-05), [[CEP20]] (-0.55, fdr 4e-05), [[GTF3C3]] (-0.52, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[WWC1]] → it (grade B ⚠); 7 go from it, the strongest it → [[PARD6B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7852.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.89×** | +31.2 | 0e+00 | 30/37 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.27×** | +29.0 | 0e+00 | 28/36 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.22×** | +16.6 | 0e+00 | 24/36 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +14.3 | 5e-44 | 23/33 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.17×** | +12.5 | 5e-34 | 24/38 (PANC-1, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +11.3 | 2e-27 | 23/37 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +6.9 | 4e-10 | 17/37 (LS 180, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +6.8 | 5e-10 | 19/35 (LS 180, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +6.4 | 9e-09 | 15/36 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +6.2 | 4e-08 | 7/22 (PANC-1, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +6.0 | 8e-08 | 15/36 (A549, NCI-H2030, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +5.6 | 1e-06 | 14/35 (PANC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +5.5 | 1e-06 | 15/37 (HCT15, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.63×** | +5.3 | 4e-06 | 12/34 (HEC-1-A, BT-474, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.002 | 7/34 (HCT15, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.026 | 5/36 (A-427, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.045 | 6/37 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.11× | +3.0 | 0.079 | 11/38 (A549, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7852.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.568×** | -11.3 | 9e-27 | 20/25 (NCI-H2030, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.638×** | -9.3 | 3e-18 | 22/37 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.661×** | -8.6 | 2e-15 | 19/30 (NCI-H2030, A498, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.764×** | -7.9 | 4e-13 | 22/38 (CFPAC-1, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.789×** | -4.9 | 1e-04 | 13/37 (RKO, NCI-H23, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.866× | -4.2 | 0.002 | 14/37 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.821×** | -4.1 | 0.004 | 9/37 (NCI-H1573, NCI-H2030, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.822×** | -4.1 | 0.004 | 18/36 (AsPC-1, SNU-423, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.824×** | -4.0 | 0.004 | 10/37 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.838× | -3.7 | 0.014 | 9/37 (NCI-H2347, NCI-H23, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.839× | -3.6 | 0.014 | 10/37 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.839× | -3.6 | 0.014 | 14/37 (HOP62, AsPC-1, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.722×** | -3.5 | 0.018 | 8/34 (HEC-1-A, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.833×** | -3.5 | 0.019 | 6/36 (HOP62, NCI-H1573, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.840× | -3.5 | 0.020 | 8/37 (NCI-H1573, CHP-212, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.741×** | -3.3 | 0.038 | 7/36 (SW480, HOP62, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7852. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 24.2 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.4× (z +37.2) | — |
| [[HEC-1-A (line)]] | alt | 54.7 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.26× (z +26.1) | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -9.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 51.8 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +28.3) | [[Dinaciclib (drug)]] 5 µM 0.146× (z -13.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 27.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.0× (z +29.8) | — |
| [[NCI-H460 (line)]] | wt | 23.9 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +16.8) | — |
| [[Panc 03.27 (line)]] | alt | 54.3 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.111× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.340× (z -9.4) |
| [[A-172 (line)]] | wt | 8.77 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +19.0) | — |
| [[CFPAC-1 (line)]] | alt | 53.8 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.208× (z -16.3) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.276× (z -9.4) |
| [[LoVo (line)]] | wt | 58.5 | 3 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.79× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.380× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 28.5 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 29.3 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 6.93× (z +13.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.46× (z +12.9) | — |
| [[SW48 (line)]] | wt | 40.8 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 6.28× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 59.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +17.1) | — |
| [[HOP62 (line)]] | alt | 11.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.8× (z +26.0) | — |
| [[J82 (line)]] | alt | 16.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.75× (z +20.2) | — |
| [[NCI-H2030 (line)]] | alt | 86.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -19.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 21.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +20.2) | — |
| [[SW1417 (line)]] | alt | 33.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -9.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 27.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +13.7) | — |
| [[A-427 (line)]] | wt | 23.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 45.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.362× (z -11.4) ⚠ cell-cycle shift, explains ~21% of this change |
| [[HepG2_C3A (line)]] | wt | 13.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.44× (z +13.1) | — |
| [[KATO III (line)]] | alt | 39.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -18.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 30.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 36.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0575× (z -18.6) |
| [[SW 900 (line)]] | alt | 13.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.29 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.24 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.34 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7852), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC2A6]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[PLEKHG3]] | +0.59 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[S100A3]] | +0.57 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[BCL3]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[EFNA1]] | +0.56 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[MB21D2]] | +0.55 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[NUAK2]] | +0.55 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[CEACAM16-AS1]] | +0.55 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[CCDC148]] | +0.54 | +0.55 / +0.39 | both halves | 5e-05 |  |
| [[IKBKE]] | +0.54 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[IFFO2]] | +0.53 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[MAP3K8]] | +0.52 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC24]] | -0.56 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[CEP20]] | -0.55 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[GTF3C3]] | -0.52 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[ELMOD2]] | -0.51 | -0.37 / -0.53 | both halves | 7e-05 |  |
| [[ZCCHC4]] | -0.50 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[EEF1AKMT2]] | -0.50 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[OPA1]] | -0.49 | -0.40 / -0.44 | both halves | 4e-05 |  |
| [[ZDHHC6]] | -0.49 | -0.31 / -0.58 | both halves | 2e-04 |  |
| [[CNIH1]] | -0.49 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[SLC30A6]] | -0.48 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[DESI2]] | -0.48 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[AGO1]] | -0.48 | -0.32 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WWC1]] | B | WWC1 activity raises USP43's level | lines that do not express WWC1 (13) vs lines expressing it (37) | 3.99× lower at baseline in the lines without WWC1 | 0.002 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CHMP4C, LSR; maybe low, not absent |
| [[EDN1]] | B | EDN1 activity raises USP43's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 3.00× lower at baseline in the lines without EDN1 | 0.005 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[RHOV]] | B | RHOV activity raises USP43's level | lines that do not express RHOV (23) vs lines expressing it (27) | 3.54× lower at baseline in the lines without RHOV | 0.007 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[EFNA1]] | B | EFNA1 activity raises USP43's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 2.22× lower at baseline in the lines without EFNA1 | 0.073 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[KMO]] | B | KMO activity raises USP43's level | lines that do not express KMO (18) vs lines expressing it (32) | 1.18× lower at baseline in the lines without KMO | 0.087 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[KRTAP5-AS1]] | C | KRTAP5-AS1 activity raises USP43's level | lines that do not express KRTAP5-AS1 (12) vs lines expressing it (38) | 3.28× lower at baseline in the lines without KRTAP5-AS1 | 0.052 | ⚠ within organs, on part of the lines; also absent: LLGL2, TFR2, USP43; maybe low, not absent; co-absent with the target |
| [[BCL9L]] | C | BCL9L activity raises USP43's level | lines that do not express BCL9L (3) vs lines expressing it (47) | 2.95× lower at baseline in the lines without BCL9L | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with SMAD3; also absent: UACA, MYH16, PER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARD6B]] | B | USP43 activity raises PARD6B's level | lines that do not express USP43 (10) vs lines expressing it (40) | 3.50× lower at baseline in the lines without USP43 | 0.008 | ⚠ within organs, on part of the lines; also absent: LLGL2, KRTAP5-AS1, BTG3-AS1 |
| [[WWC1]] | B | USP43 activity raises WWC1's level | lines that do not express USP43 (10) vs lines expressing it (40) | 3.85× lower at baseline in the lines without USP43 | 0.014 | ⚠ within organs, on part of the lines; also absent: LLGL2, KRTAP5-AS1, BTG3-AS1 |
| [[EDN1]] | B | USP43 activity raises EDN1's level | lines that do not express USP43 (10) vs lines expressing it (40) | 4.06× lower at baseline in the lines without USP43 | 0.024 | ⚠ within organs, on part of the lines; also absent: LLGL2, KRTAP5-AS1, BTG3-AS1 |
| [[PARD6B]] | B | USP43 activity strengthens PARD6B's drug response | lines that do not express USP43 (6) vs lines expressing it (36) | the lines without USP43 respond 0.84× as strongly (z diff +0.92); strongest at Homoharringtonine 0.5 µM: 1.34x vs 2.06x (z diff +4.0) | 0.089 | ⚠ within organs, on part of the lines; also absent: LLGL2, KRTAP5-AS1, BTG3-AS1; target measured in part of the lines; both ways; artifact flags |
| [[HLA-F]] | B | USP43 activity raises HLA-F's level | lines that do not express USP43 (10) vs lines expressing it (40) | 1.77× lower at baseline in the lines without USP43 | 0.093 | ⚠ within organs, on part of the lines; also absent: LLGL2, KRTAP5-AS1, BTG3-AS1 |
| [[RHOV]] | B | USP43 activity raises RHOV's level | lines that do not express USP43 (10) vs lines expressing it (40) | 2.89× lower at baseline in the lines without USP43 | 0.093 | ⚠ within organs, on part of the lines; also absent: LLGL2, KRTAP5-AS1, BTG3-AS1 |
| [[DDR1]] | B | USP43 activity raises DDR1's level | lines that do not express USP43 (10) vs lines expressing it (40) | 2.09× lower at baseline in the lines without USP43 | 0.096 | ⚠ within organs, on part of the lines; also absent: LLGL2, KRTAP5-AS1, BTG3-AS1 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.617). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.6, 7.1); signed map (43.8, 4.1). **Vector** length 95.9, 22.5% of its response variance represented; |z| ≥ 3 in 863 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.2 | +29.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +31.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +11.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.9 | +12.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.1 | +16.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +6.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +3.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +5.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.8 | -9.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -5.1 | -7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.3 | -11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.2 | -8.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -4.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 43 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:9,644,698-9,729,687 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30626 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Reactome | 4 pathways, smallest: Termination of translesion DNA synthesis; Translesion synthesis by Y family DNA polymerases bypasses lesions on DNA template; DNA Damage Bypass |
| Matched by | ensembl_id |

**Function**, from UniProt [Q70EL4](https://www.uniprot.org/uniprotkb/Q70EL4) (Ubiquitin carboxyl-terminal hydrolase 43):

> May recognize and hydrolyze the peptide bond at the C-terminal Gly of ubiquitin. Involved in the processing of poly-ubiquitin precursors as well as that of ubiquitinated proteins (By similarity).

**Summary**, from NCBI Gene [124739](https://www.ncbi.nlm.nih.gov/gene/124739):

> Predicted to enable ISG15-specific peptidase activity. Predicted to be involved in translesion synthesis. Predicted to be located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20072](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20072) · Entrez [124739](https://www.ncbi.nlm.nih.gov/gene/124739) · UniProt [Q70EL4](https://www.uniprot.org/uniprotkb/Q70EL4) · Ensembl [ENSG00000154914](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154914)

## Data

Gene col 7852: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7852); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7852, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7852]; `tensor/DDL_lfc|DDL_z.npy` [7852]; `embed/gene_vectors.npy` [7852]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7852 or target_col == 7852). Every well: [[USP43 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP43.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
