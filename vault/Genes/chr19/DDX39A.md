---
symbol: "DDX39A"
type: "gene"
col: 4406
ensembl_id: "ENSG00000123136"
name: "DExD-box helicase 39A"
location: "19p13.12"
module: 3
arm: "-"
pooled_cpm: 23.88
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# DDX39A

*DExD-box helicase 39A* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.56× (z +25.0, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Carbidopa (monohydrate) (drug)]] 0.05 µM: 0.691× (z -5.2, q 1e-04, down in 28 of 48 measured lines) ⚠ unreliable plate only; position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM in 1 line (H4 0.121×; ⚠ cell-cycle shift, would explain all of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.105×); [[Vandetanib (drug)]] 5 µM in 1 line (SW48 0.132×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPL]] (+0.65, fdr 1e-05), [[CTBP1-DT]] (+0.64, fdr 1e-05), [[PTBP1]] (+0.61, fdr 1e-05); moves opposite to [[ELOB]] (-0.56, fdr 2e-05), [[DPY30]] (-0.55, fdr 3e-05), [[CIAO2B]] (-0.55, fdr 2e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4406.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.56×** | +25.0 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.66×** | +18.0 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **7.49×** | +14.6 | 0e+00 | 48/48 (PANC-1, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.79×** | +14.2 | 7e-44 | 44/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.59×** | +12.7 | 5e-35 | 43/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.41×** | +11.8 | 6e-30 | 43/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **4.94×** | +11.6 | 3e-29 | 41/47 (HEC-1-A, C32, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +11.2 | 2e-27 | 37/47 (Panc 03.27, LoVo, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.10×** | +10.3 | 3e-23 | 41/47 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.06×** | +8.8 | 1e-16 | 36/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.99×** | +8.4 | 2e-15 | 34/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.76×** | +7.3 | 2e-11 | 28/37 (LoVo, PANC-1, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +7.1 | 5e-11 | 32/47 (SW480, LoVo, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.57×** | +6.3 | 1e-08 | 27/43 (LoVo, A-427, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.50×** | +5.6 | 8e-07 | 24/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +5.6 | 9e-07 | 28/47 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.005 | 18/48 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.026 | 14/46 (Hs 766T, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.026 | 12/48 (BT-474, NCI-H2030, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.033 | 16/47 (LoVo, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4406.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM in 1 line (H4 0.121×; ⚠ cell-cycle shift, would explain all of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.105×); [[Vandetanib (drug)]] 5 µM in 1 line (SW48 0.132×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.691×** | -5.2 | 1e-04 | 28/48 (Panc 03.27, HS-578T, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.776× | -3.5 | 0.11 | 13/47 (Panc 03.27, A-172, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.795× | -3.1 | 0.37 | 12/47 (A549, COLO 205, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4406. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.5 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.55× (z +19.9) | — |
| [[LoVo (line)]] | wt | 19.1 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +15.1) | — |
| [[PANC-1 (line)]] | alt | 23.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +20.5) | — |
| [[KATO III (line)]] | alt | 14.0 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 10.6× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 10.3× (z +14.2) | — |
| [[NCI-H2347 (line)]] | alt | 24.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +14.3) | — |
| [[AsPC-1 (line)]] | alt | 18.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +11.5) | — |
| [[LS 180 (line)]] | wt | 17.5 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.77× (z +12.6) | — |
| [[NCI-H1573 (line)]] | alt | 9.99 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +12.3) | — |
| [[NCI-H2030 (line)]] | alt | 44.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +12.3) | — |
| [[Panc 03.27 (line)]] | alt | 33.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +15.1) | — |
| [[SW1417 (line)]] | alt | 25.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +12.1) | — |
| [[SW480 (line)]] | alt | 23.5 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +11.0) | — |
| [[A-172 (line)]] | wt | 35.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +14.9) | — |
| [[HEC-1-A (line)]] | alt | 22.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +12.6) | — |
| [[HOP62 (line)]] | alt | 15.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 34.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +14.1) | — |
| [[hTERT-HPNE (line)]] | wt | 15.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +10.2) | [[Hydroxyurea (drug)]] 0.05 µM 0.105× (z -9.2) |
| [[J82 (line)]] | alt | 28.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +14.6) | — |
| [[LOX-IMVI (line)]] | wt | 14.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 23.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +16.1) | — |
| [[SW 900 (line)]] | alt | 21.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +9.1) | — |
| [[A498 (line)]] | wt | 47.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +15.7) | — |
| [[A549 (line)]] | wt | 19.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +11.9) | — |
| [[BT-474 (line)]] | alt | 33.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.01× (z +8.9) | — |
| [[C32 (line)]] | wt | 14.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.56× (z +13.0) | — |
| [[CFPAC-1 (line)]] | alt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +10.8) | — |
| [[COLO 205 (line)]] | alt | 19.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +9.6) | — |
| [[H4 (line)]] | wt | 30.9 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.121× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 17.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +12.5) | — |
| [[NCI-H1792 (line)]] | alt | 13.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +10.2) | — |
| [[RKO (line)]] | wt | 26.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +11.9) | — |
| [[RPMI-7951 (line)]] | alt | 32.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 24.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +11.6) | — |
| [[SW48 (line)]] | wt | 18.1 | 0 | 1 | — | [[Vandetanib (drug)]] 5 µM 0.132× (z -8.7) |
| [[A-427 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4406), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPL]] | +0.65 | +0.67 / +0.56 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 531 |
| [[CTBP1-DT]] | +0.64 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[PTBP1]] | +0.61 | +0.50 / +0.65 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 401 |
| [[U2AF2]] | +0.61 | +0.50 / +0.54 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 828 |
| [[HNRNPUL1]] | +0.61 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[ALDH16A1]] | +0.60 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[REXO5]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[FOXM1]] | +0.58 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[CTBP1]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[NCAPH2]] | +0.57 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[SRSF1]] | +0.57 | +0.55 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_E2F_TARGETS; STRING 543 |
| [[PHF19]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELOB]] | -0.56 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[DPY30]] | -0.55 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[CIAO2B]] | -0.55 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[GAN]] | -0.54 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[ATP5MJ]] | -0.54 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ZYG11B]] | -0.53 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[SLC35A1]] | -0.53 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[RPS5]] | -0.52 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[PCTP]] | -0.52 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[CAMLG]] | -0.52 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[MRPL41]] ⚠ | -0.52 | -0.49 / -0.40 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RBIS]] | -0.51 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[COX6A1]] | -0.51 | -0.45 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.450). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-40.8, -32.4); signed map (-9.2, -34.8). **Vector** length 74.6, 17.2% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dengue Virus-Host Interactions* (reactome, mean cos +0.51 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +6.9 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | +6.7 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | +6.3 | +6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +11.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +25.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +7.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +11.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +3.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | +0.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.7 | +5.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | +0.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | DExD-box helicase 39A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:14,408,798-14,419,383 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DDXL, BAT1L, URH49; previously DDX39 |
| Gene groups (HGNC) | DEAD-box helicases; Transcription and export complex 1 subunits |
| Hallmark sets | MTORC1_SIGNALING, G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 5 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; mRNA 3'-end processing |
| Matched by | ensembl_id |

**Function**, from UniProt [O00148](https://www.uniprot.org/uniprotkb/O00148) (ATP-dependent RNA helicase DDX39A):

> Helicase that plays an essential role in mRNA export and is involved in multiple steps in RNA metabolism including alternative splicing. Regulates nuclear mRNA export to the cytoplasm through association with ECD. Also involved in spliceosomal uridine-rich small nuclear RNA (U snRNA) export by stimulating the RNA binding of adapter PHAX. Plays a role in the negative regulation of type I IFN production by increasing the nuclear retention of antiviral transcripts and thus reducing their protein …

**Summary**, from NCBI Gene [10212](https://www.ncbi.nlm.nih.gov/gene/10212):

> This gene encodes a member of the DEAD box protein family. These proteins are characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD) and are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure, such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of the DEAD box protein family are believed to be involved in …

**Accessions** — [HGNC:17821](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17821) · Entrez [10212](https://www.ncbi.nlm.nih.gov/gene/10212) · UniProt [O00148](https://www.uniprot.org/uniprotkb/O00148) · Ensembl [ENSG00000123136](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123136)

## Data

Gene col 4406: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4406); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4406, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4406]; `tensor/DDL_lfc|DDL_z.npy` [4406]; `embed/gene_vectors.npy` [4406]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4406 or target_col == 4406). Every well: [[DDX39A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX39A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
