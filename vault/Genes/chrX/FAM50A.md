---
symbol: "FAM50A"
type: "gene"
col: 993
ensembl_id: "ENSG00000071859"
name: "family with sequence similarity 50 member A"
location: "Xq28"
module: 123
arm: "+"
pooled_cpm: 31.85
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 4
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# FAM50A

*family with sequence similarity 50 member A* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.15× (z +13.0, q 6e-36, up in 33 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.66× (z +5.9, q 4e-07, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Anethole trithione (drug)]] 0.5 µM: 0.668× (z -4.8, q 1e-03, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARVCF]] (+0.65, fdr 7e-06), [[TFE3]] (+0.64, fdr 1e-05), [[AMDHD2]] (+0.62, fdr 1e-05); moves opposite to [[PHC2-AS1]] (-0.54, fdr 7e-05), [[C14orf93]] (-0.52, fdr 9e-04, ⚠ not reproduced), [[NAF1]] (-0.51, fdr 4e-05), [[LEMD3]] (-0.51, fdr 6e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 993.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.15×** | +13.0 | 6e-36 | 33/35 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.90×** | +12.5 | 1e-33 | 43/43 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.32×** | +9.2 | 9e-18 | 36/39 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.66×** | +5.9 | 4e-07 | 32/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +5.6 | 2e-06 | 35/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +5.0 | 5e-05 | 28/48 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.50×** | +4.8 | 1e-04 | 34/45 (RPMI-7951, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.34×** | +4.6 | 3e-04 | 32/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +4.5 | 5e-04 | 23/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +4.4 | 7e-04 | 27/47 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.47×** | +4.4 | 7e-04 | 31/48 (NCI-H1573, NCI-H460, …) | two highest doses | composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.3 | 8e-04 | 0/48 | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +4.2 | 0.001 | 25/48 (HT-29, NCI-H1792, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.003 | 26/48 (AsPC-1, HT-29, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.36×** | +3.6 | 0.013 | 21/47 (HT-29, HOP62, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.76×** | +3.5 | 0.017 | 23/48 (HT-29, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.027 | 19/47 (HT-29, LoVo, …) | inconsistent across doses | position effect removed |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.069 | 15/48 (C32, PANC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 993.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.668×** | -4.8 | 1e-03 | 37/48 (SW1417, PANC-1, …) | two highest doses | position effect removed |
| [[Minodronic acid (drug)]] 0.05 µM |  | **0.708×** | -3.8 | 0.036 | 27/48 (PANC-1, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.711×** | -3.7 | 0.036 | 23/47 (HS-578T, RKO, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.794×** | -3.6 | 0.040 | 24/47 (SK-MEL-2, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.597× | -3.2 | 0.16 | 19/47 (RKO, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.817× | -3.1 | 0.17 | 13/48 (NCI-H2347, HT-29, …) | two highest doses | position effect removed |
| [[Pemetrexed (drug)]] 0.5 µM |  | 0.773× | -3.1 | 0.18 | 15/47 (SNU-423, PANC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 993. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 33.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +11.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 25.1 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +11.8) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[PANC-1 (line)]] | alt | 44.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +14.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 21.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.75× (z +12.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 54.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.4) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[A498 (line)]] | wt | 38.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +9.2) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 37.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.64× (z +10.3) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 27.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +9.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 39.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.44× (z +11.1) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 63.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +10.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 35.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +10.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 24.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +9.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 27.3 | 0 | 1 | — | [[Voriconazole (drug)]] 0.5 µM 0.0622× (z -9.3) |
| [[C32 (line)]] | wt | 15.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.53× (z +9.4) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 25.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +8.5) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 18.6 | 0 | 1 | — | [[Vandetanib (drug)]] 5 µM 0.0521× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 24.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.57× (z +10.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 22.1 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.121× (z -8.8) |
| [[HT-29 (line)]] | alt | 47.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 27.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 37.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 39.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -9.2) |
| [[SW 900 (line)]] | alt | 33.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +8.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 993), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARVCF]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[TFE3]] | +0.64 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[AMDHD2]] | +0.62 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[HS1BP3]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[DUSP8]] | +0.61 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[JUND]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[DNAJB2]] | +0.58 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[PPP1R12C]] | +0.57 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[PLXNA3]] | +0.57 | +0.44 / +0.51 | both halves | 3e-05 | ⚠ same locus (7.6 kb, same strand: neighbours can correlate without regulation) |
| [[RHOB]] | +0.56 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[CC2D1B]] | +0.56 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[DLGAP4]] | +0.56 | +0.39 / +0.55 | both halves | 6e-05 |  |
| [[SHC2]] | +0.56 | +0.43 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHC2-AS1]] | -0.54 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[C14orf93]] | -0.52 | -0.18 / -0.43 | ⚠ not reproduced | 9e-04 |  |
| [[NAF1]] | -0.51 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[LEMD3]] | -0.51 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[C21orf58]] | -0.50 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[XNDC1N]] | -0.50 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | -0.50 | -0.25 / -0.44 | both halves | 4e-04 |  |
| [[HSPA14]] | -0.49 | -0.29 / -0.53 | both halves | 3e-04 |  |
| [[SNHG30]] | -0.49 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[FANCM]] | -0.48 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[TSHZ1]] | -0.48 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[KLHL3]] | -0.48 | -0.25 / -0.51 | both halves | 4e-04 | same gene group |
| [[ZBTB11]] | -0.47 | -0.23 / -0.42 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.417). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.7, -3.0); signed map (-4.6, 22.1). **Vector** length 77.6, 19.2% of its response variance represented; |z| ≥ 3 in 619 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.2 | +4.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.1 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.9 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +2.8 | +4.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.3 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -0.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.8 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | +0.4 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.4 | +0.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -3.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 50 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:154,444,141-154,450,654 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DXS9928E, XAP5, HXC-26, 9F |
| Gene groups (HGNC) | Spliceosomal C complex; Spliceosomal P complex; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14320](https://www.uniprot.org/uniprotkb/Q14320) (Protein FAM50A):

> Probably involved in the regulation of pre-mRNA splicing.

**Summary**, from NCBI Gene [9130](https://www.ncbi.nlm.nih.gov/gene/9130):

> This gene belongs to the FAM50 family. The encoded protein is highly conserved in length and sequence across different species. It is a basic protein containing a nuclear localization signal, and may function as a DNA-binding protein or a transcriptional factor. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:18786](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18786) · Entrez [9130](https://www.ncbi.nlm.nih.gov/gene/9130) · UniProt [Q14320](https://www.uniprot.org/uniprotkb/Q14320) · Ensembl [ENSG00000071859](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071859)

## Data

Gene col 993: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 993); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 993, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 993]; `tensor/DDL_lfc|DDL_z.npy` [993]; `embed/gene_vectors.npy` [993]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 993 or target_col == 993). Every well: [[FAM50A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM50A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
