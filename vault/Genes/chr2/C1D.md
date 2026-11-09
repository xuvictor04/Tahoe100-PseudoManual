---
symbol: "C1D"
type: "gene"
col: 12366
ensembl_id: "ENSG00000197223"
name: "C1D nuclear receptor corepressor"
location: "2p14"
module: 20
arm: "+"
pooled_cpm: 24.57
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# C1D

*C1D nuclear receptor corepressor* — 2p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.17× (z +12.3, q 4e-32, up in 42 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (A-427 0.233×, LS 180 0.193×, Panc 03.27 0.207×, SHP-77 0.262×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 1 line (H4 0.139×; ⚠ transcription drop; cell-cycle shift, explains ~13% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.236×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.177×); [[CP21R7 (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0617×).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDHD]] (+0.78, fdr 7e-06), [[ZBTB26]] (+0.67, fdr 1e-05), [[EIF3F]] (+0.66, fdr 1e-05); moves opposite to [[ORAI1]] (-0.55, fdr 1e-05), [[LRRC8E]] (-0.52, fdr 1e-04), [[TNFRSF1B]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12366.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.17×** | +12.3 | 4e-32 | 42/48 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.57×** | +10.1 | 2e-21 | 35/47 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +9.3 | 4e-18 | 33/48 (HEC-1-A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.50×** | +8.2 | 2e-14 | 35/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +8.0 | 1e-13 | 32/48 (A-172, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.40×** | +6.4 | 2e-08 | 21/40 (A498, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +5.9 | 3e-07 | 23/48 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +5.8 | 5e-07 | 22/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.9 | 4e-05 | 12/30 (SW480, A-172, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +4.9 | 4e-05 | 17/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +4.6 | 2e-04 | 15/45 (SNU-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +4.5 | 3e-04 | 21/47 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.24×** | +4.5 | 3e-04 | 20/43 (NCI-H1792, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.003 | 14/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +3.8 | 0.005 | 12/37 (A-172, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.007 | 11/48 (LoVo, A498, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.008 | 9/46 (A498, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.014 | 8/48 (SK-MEL-2, PANC-1, …) | two highest doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.19× | +3.4 | 0.018 | 8/47 (LOX-IMVI, SW1417, …) | top dose only |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.021 | 13/46 (A-427, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Asciminib (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.034 | 11/48 (A-427, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12366.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (A-427 0.233×, LS 180 0.193×, Panc 03.27 0.207×, SHP-77 0.262×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 1 line (H4 0.139×; ⚠ transcription drop; cell-cycle shift, explains ~13% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.236×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.177×); [[CP21R7 (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0617×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.844× | -3.5 | 0.30 | 13/48 (A549, SW480, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.898× | -3.1 | 0.47 | 12/48 (SW480, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12366. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 42.1 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +12.8) | — |
| [[SW480 (line)]] | alt | 24.0 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 4.88× (z +9.8) | — |
| [[A-427 (line)]] | wt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -12.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 53.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -9.7) |
| [[H4 (line)]] | wt | 29.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.139× (z -10.5) ⚠ transcription drop; cell-cycle shift, explains ~13% of this change |
| [[HCT15 (line)]] | alt | 22.2 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.177× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 20.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 20.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 23.0 | 0 | 1 | — | [[CP21R7 (drug)]] 5 µM 0.0617× (z -8.5) |
| [[LS 180 (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 27.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 24.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -9.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -9.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12366), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHD]] | +0.78 | +0.69 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[ZBTB26]] | +0.67 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[EIF3F]] | +0.66 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[MRPS22]] | +0.66 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[NAXD]] | +0.64 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[SUMO1]] | +0.63 | +0.57 / +0.70 | both halves | 9e-06 |  |
| [[COPS7B]] | +0.63 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[EIF2B1]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[MSL3]] | +0.62 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[DDOST]] | +0.61 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[RAE1]] | +0.61 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[ZNF596]] | +0.61 | +0.23 / +0.65 | both halves | 5e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ORAI1]] | -0.55 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[LRRC8E]] | -0.52 | -0.34 / -0.60 | both halves | 1e-04 |  |
| [[TNFRSF1B]] | -0.51 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[JUND]] | -0.51 | -0.35 / -0.53 | both halves | 1e-04 | pathway: Affinity selection of immunoglobulins |
| [[TUBB2B]] | -0.51 | -0.30 / -0.49 | both halves | 2e-04 | pathway: Affinity selection of immunoglobulins |
| [[KLF2]] | -0.50 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[PPP1R13B]] | -0.50 | -0.40 / -0.45 | both halves | 4e-05 |  |
| [[PPFIA1]] | -0.48 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[PIP5K1C]] | -0.48 | -0.37 / -0.45 | both halves | 9e-05 |  |
| [[CLEC16A]] | -0.48 | -0.27 / -0.56 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.521). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-20.1, -15.5); signed map (-18.6, -30.9). **Vector** length 71.6, 11.9% of its response variance represented; |z| ≥ 3 in 881 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.8 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +10.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.4 | -0.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +0.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -0.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.0 | +0.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -1.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | C1D nuclear receptor corepressor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p14 — chr2:68,041,130-68,110,948 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SUNCOR, SUN-CoR, LRP1, Rrp47 |
| Reactome | 9 pathways, smallest: Nuclear RNA decay; Somatic hypermutation of immunoglobulin genes; Major pathway of rRNA processing in the nucleolus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13901](https://www.uniprot.org/uniprotkb/Q13901) (Nuclear nucleic acid-binding protein C1D):

> Plays a role in the recruitment of the RNA exosome complex to pre-rRNA to mediate the 3'-5' end processing of the 5.8S rRNA; this function may include MPHOSPH6. Can activate PRKDC not only in the presence of linear DNA but also in the presence of supercoiled DNA. Can induce apoptosis in a p53/TP53 dependent manner. May regulate the TRAX/TSN complex formation. Potentiates transcriptional repression by NR1D1 and THRB (By similarity).

**Summary**, from NCBI Gene [10438](https://www.ncbi.nlm.nih.gov/gene/10438):

> The protein encoded by this gene is a DNA binding and apoptosis-inducing protein and is localized in the nucleus. It is also a Rac3-interacting protein which acts as a corepressor for the thyroid hormone receptor. This protein is thought to regulate TRAX/Translin complex formation. Alternate splicing results in multiple transcript variants that encode the same protein. Multiple pseudogenes of this gene are found on chromosome 10.[provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:29911](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29911) · Entrez [10438](https://www.ncbi.nlm.nih.gov/gene/10438) · UniProt [Q13901](https://www.uniprot.org/uniprotkb/Q13901) · Ensembl [ENSG00000197223](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197223)

## Data

Gene col 12366: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12366); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12366, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12366]; `tensor/DDL_lfc|DDL_z.npy` [12366]; `embed/gene_vectors.npy` [12366]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12366 or target_col == 12366). Every well: [[C1D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
