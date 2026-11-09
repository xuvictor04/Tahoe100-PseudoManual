---
symbol: "SFXN5"
type: "gene"
col: 6838
ensembl_id: "ENSG00000144040"
name: "sideroflexin 5"
location: "2p13.2"
module: 47
arm: "+"
pooled_cpm: 31.98
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# SFXN5

*sideroflexin 5* — 2p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.93× (z +15.0, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.623× (z -6.4, q 1e-07, down in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.697× (z -5.0, q 1e-04, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHTF1]] (+0.72, fdr 7e-06), [[VCP]] (+0.70, fdr 7e-06), [[FERMT3]] (+0.67, fdr 7e-06); moves opposite to [[MRPS31P4]] (-0.60, fdr 1e-05), [[UBXN2B]] (-0.59, fdr 1e-05), [[ZNF14]] (-0.59, fdr 3e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6838.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.93×** | +15.0 | 0e+00 | 45/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.78×** | +14.2 | 2e-43 | 45/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +12.3 | 2e-32 | 41/47 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.71×** | +12.1 | 2e-31 | 43/48 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +8.9 | 8e-17 | 39/48 (A-172, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.9 | 4e-10 | 33/48 (MIA PaCa-2, A549, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.49×** | +5.3 | 8e-06 | 31/47 (NCI-H460, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.68×** | +5.2 | 2e-05 | 30/48 (SW480, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.89×** | +4.6 | 2e-04 | 24/43 (SW480, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.39×** | +4.4 | 6e-04 | 18/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +4.4 | 6e-04 | 21/48 (A549, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.33×** | +4.0 | 0.003 | 24/48 (A549, PANC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.33×** | +3.9 | 0.004 | 19/48 (SW480, RKO, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.033 | 15/47 (H4, HepG2/C3A, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.58×** | +3.3 | 0.034 | 15/48 (RKO, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Demeclocycline (drug)]] 5 µM |  | 1.17× | +3.0 | 0.079 | 10/48 (HS-578T, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6838.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.623×** | -6.4 | 1e-07 | 31/48 (A-427, KATO III, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.697×** | -5.0 | 1e-04 | 24/48 (KATO III, PANC-1, …) | top dose only | cell-cycle shift (explains ~20% here); composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.531×** | -4.6 | 7e-04 | 25/47 (KATO III, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.729×** | -4.4 | 0.001 | 24/48 (C32, A-427, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.567×** | -4.1 | 0.004 | 23/48 (A-427, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | **0.760×** | -3.8 | 0.012 | 24/45 (SW 900, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.766×** | -3.6 | 0.027 | 18/36 (Hs 766T, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.780×** | -3.5 | 0.037 | 20/47 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | 0.851× | -3.2 | 0.090 | 14/48 (Hs 766T, HEC-1-A, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.800× | -3.0 | 0.15 | 19/47 (NCI-H2347, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, -0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6838. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 36.2 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.119× (z -17.0) |
| [[A-427 (line)]] | wt | 51.7 | 0 | 5 (3 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0295× (z -17.0) |
| [[NCI-H460 (line)]] | wt | 38.2 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +14.5) | — |
| [[SW480 (line)]] | alt | 19.3 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.58× (z +13.2) | — |
| [[A498 (line)]] | wt | 35.6 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +12.0) | — |
| [[A549 (line)]] | wt | 27.9 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +13.0) | — |
| [[COLO 205 (line)]] | alt | 35.1 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 5.89× (z +11.1) | [[Harringtonine (drug)]] 5 µM 0.230× (z -8.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HOP62 (line)]] | alt | 36.6 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.77× (z +12.7) | — |
| [[NCI-H1573 (line)]] | alt | 20.1 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +11.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +8.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.224× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 53.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 51.9 | 3 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.48× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 36.9 | 2 | 2 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.02× (z +9.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -12.8) |
| [[LoVo (line)]] | wt | 22.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.10× (z +10.6) | — |
| [[LOX-IMVI (line)]] | wt | 43.8 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.261× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 36.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.63× (z +18.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.39× (z +10.1) | — |
| [[RKO (line)]] | wt | 24.5 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +11.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.147× (z -12.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 48.0 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.83× (z +9.3) | — |
| [[BT-474 (line)]] | alt | 25.0 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.195× (z -9.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HEC-1-A (line)]] | alt | 36.0 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.89× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 33.0 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.25× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 37.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -10.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 29.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.251× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 24.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.29× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 40.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +15.0) ⚠ cell-cycle shift, would explain all of this change | [[Docetaxel (drug)]] 0.05 µM 0.250× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~59% of this change |
| [[SW1417 (line)]] | alt | 21.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 31.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +13.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 59.0 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.07× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 27.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Hs 766T (line)]] | wt | 23.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -12.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 37.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 39.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 42.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.274× (z -9.4) ⚠ transcription drop; cell-cycle shift, explains ~59% of this change |
| [[SW48 (line)]] | wt | 13.0 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.0635× (z -9.6) |
| [[AN3 CA (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6838), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHTF1]] | +0.72 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[VCP]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[FERMT3]] | +0.67 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[MSANTD1]] | +0.67 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[SLC22A20P]] | +0.64 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[LINC01588]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[MPP4]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[HSP90AA2P]] | +0.62 | +0.66 / +0.58 | both halves | 8e-06 |  |
| [[LINC02798]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[YIPF7]] | +0.61 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[PIP5KL1]] | +0.61 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[SERPINH1]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS31P4]] | -0.60 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[UBXN2B]] | -0.59 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[ZNF14]] | -0.59 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[PEX2]] | -0.58 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[GEMIN2]] | -0.58 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[NIPSNAP2]] | -0.57 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[DOP1A]] | -0.57 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[TRAPPC11]] | -0.56 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[YY1AP1]] | -0.56 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[THOC1]] | -0.55 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[ARHGAP12]] | -0.55 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[XPA]] | -0.55 | -0.37 / -0.60 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SFXN5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[B4GALNT1]] | B | B4GALNT1 activity raises SFXN5's level | lines that do not express B4GALNT1 (16) vs lines expressing it (34) | 1.56× lower at baseline in the lines without B4GALNT1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1 |
| [[SCUBE2]] | B | SCUBE2 activity raises SFXN5's level | lines that do not express SCUBE2 (7) vs lines expressing it (43) | 1.67× lower at baseline in the lines without SCUBE2 | 0.039 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| [[PLEKHA6]] | B | PLEKHA6 activity lowers SFXN5's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.44× higher at baseline in the lines without PLEKHA6 | 0.059 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.570). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.1, -20.4); signed map (14.6, 15.4). **Vector** length 121, 33.9% of its response variance represented; |z| ≥ 3 in 1,131 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +12.4 | +15.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +11.4 | +12.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +11.3 | +14.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.9 | +8.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | +7.1 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +6.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.6 | +5.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.6 | +3.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | -2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -4.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -4.9 | -6.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -2.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[Bexarotene (drug)]] 5 µM |  | -2.8 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.7 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | sideroflexin 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.2 — chr2:72,942,036-73,075,619 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BBG-TCC, SLC56A5 |
| Gene groups (HGNC) | Solute carrier family 56, sideroflexins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TD22](https://www.uniprot.org/uniprotkb/Q8TD22) (Sideroflexin-5):

> Mitochondrial amino-acid transporter (By similarity). Transports citrate (By similarity). Does not act as a serine transporter: not able to mediate transport of serine into mitochondria (By similarity). In brown adipose tissue, plays a role in the regulation of UCP1-dependent thermogenesis probably by supporting mitochondrial glycerol-3-phosphate utilization (By similarity).

**Summary**, from NCBI Gene [94097](https://www.ncbi.nlm.nih.gov/gene/94097):

> Predicted to enable citrate transmembrane transporter activity. Predicted to be involved in citrate transport and mitochondrial transmembrane transport. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16073](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16073) · Entrez [94097](https://www.ncbi.nlm.nih.gov/gene/94097) · UniProt [Q8TD22](https://www.uniprot.org/uniprotkb/Q8TD22) · Ensembl [ENSG00000144040](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144040)

## Data

Gene col 6838: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6838); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6838, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6838]; `tensor/DDL_lfc|DDL_z.npy` [6838]; `embed/gene_vectors.npy` [6838]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6838 or target_col == 6838). Every well: [[SFXN5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SFXN5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
