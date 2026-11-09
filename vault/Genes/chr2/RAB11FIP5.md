---
symbol: "RAB11FIP5"
type: "gene"
col: 5733
ensembl_id: "ENSG00000135631"
name: "RAB11 family interacting protein 5"
location: "2p13.2"
module: 180
arm: "+"
pooled_cpm: 34.87
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 15
n_dd_up_clean: 17
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/180"]
generated_by: "tahoemap"
---

# RAB11FIP5

*RAB11 family interacting protein 5* — 2p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.51× (z +7.1, q 1e-09, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.409× (z -10.9, q 4e-25, down in 27 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.521× (z -8.0, q 3e-13, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAHD1]] (+0.68, fdr 1e-05), [[RAB6A]] (+0.67, fdr 7e-06), [[RALGDS]] (+0.67, fdr 7e-06); moves opposite to [[SRSF10]] (-0.60, fdr 3e-05), [[XRCC5]] (-0.59, fdr 3e-05), [[UTP20]] (-0.59, fdr 1e-05).
> It is in [[Module 180]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NRTN]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5733.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +7.1 | 1e-09 | 30/47 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.40×** | +5.8 | 2e-06 | 35/48 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +5.0 | 1e-04 | 31/48 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.42×** | +4.4 | 0.002 | 28/48 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.2 | 0.002 | 30/48 (NCI-H23, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +4.1 | 0.004 | 28/48 (PANC-1, LS 180, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.38×** | +4.0 | 0.004 | 27/48 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +4.0 | 0.004 | 27/48 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.52×** | +3.8 | 0.010 | 24/47 (LS 180, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.50×** | +3.6 | 0.016 | 20/48 (SW 900, hTERT-HPNE, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.016 | 21/48 (CFPAC-1, NCI-H460, …) | top dose only | plate-row cell shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +3.6 | 0.016 | 22/48 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.33×** | +3.6 | 0.016 | 23/47 (NCI-H1573, SK-MEL-2, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.024 | 22/48 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +3.3 | 0.033 | 15/41 (HCT15, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Fumaric acid (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.061 | 18/48 (LOX-IMVI, CFPAC-1, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.062 | 12/48 (HS-578T, hTERT-HPNE, …) | top dose only | plate-row cell shift |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.072 | 13/48 (NCI-H2347, A-172, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5733.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.409×** | -10.9 | 4e-25 | 27/36 (AsPC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.450×** | -10.1 | 1e-21 | 39/46 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.521×** | -8.0 | 3e-13 | 38/48 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.599×** | -6.0 | 2e-07 | 27/43 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.780×** | -4.4 | 0.001 | 25/48 (J82, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **0.723×** | -4.1 | 0.004 | 28/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.735×** | -3.9 | 0.007 | 23/48 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.754×** | -3.6 | 0.023 | 24/48 (A498, C-33 A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.770×** | -3.3 | 0.054 | 21/47 (NCI-H2347, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.773×** | -3.3 | 0.056 | 20/48 (NCI-H1573, LOX-IMVI, …) | all doses, flat |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.784×** | -3.1 | 0.096 | 12/48 (NCI-H2347, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Busulfan (drug)]] 0.05 µM |  | **0.786×** | -3.1 | 0.096 | 14/48 (A549, SW1417, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.836× | -3.1 | 0.096 | 16/48 (RPMI-7951, LS 180, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.782×** | -3.0 | 0.096 | 19/48 (NCI-H23, NCI-H2347, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.637×** | -3.0 | 0.096 | 16/47 (AN3 CA, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5733. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 33.9 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.325× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 29.5 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.13× (z +21.4) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.29× (z +11.0) | — |
| [[AsPC-1 (line)]] | alt | 53.2 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.365× (z -8.9) |
| [[A498 (line)]] | wt | 42.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +11.6) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.182× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 27.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +24.1) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 2.71× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -10.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 47.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +18.1) ⚠ cell-cycle shift, explains ~52% of this change | [[Dinaciclib (drug)]] 5 µM 0.316× (z -9.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 71.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.100× (z -19.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 21.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.183× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 36.5 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.38× (z +18.5) ⚠ cell-cycle shift, explains ~52% of this change | [[Belumosudil (drug)]] 5 µM 0.259× (z -9.5) |
| [[A-172 (line)]] | wt | 73.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -9.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 41.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.80× (z +22.2) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[CFPAC-1 (line)]] | alt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -10.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 48.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0918× (z -13.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 31.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +18.1) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[HEC-1-A (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -15.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 34.9 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.166× (z -9.2) |
| [[HS-578T (line)]] | alt | 51.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +9.6) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[J82 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.226× (z -13.2) ⚠ cell-cycle shift, explains ~18% of this change |
| [[LoVo (line)]] | wt | 22.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 46.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 42.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +25.4) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[NCI-H2030 (line)]] | alt | 48.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +12.0) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[Panc 03.27 (line)]] | alt | 27.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -10.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 50.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.180× (z -11.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 36.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.6× (z +25.0) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[SW1417 (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0674× (z -10.2) ⚠ toxic |
| [[SW48 (line)]] | wt | 30.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -10.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 10.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +8.9) | — |
| [[A-427 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5733), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAHD1]] | +0.68 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[RAB6A]] | +0.67 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[RALGDS]] | +0.67 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[ENO2]] | +0.66 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[STK32C]] | +0.63 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[INSIG2]] | +0.63 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[PPP2R5B]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[CNOT8]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[WDR45B]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[MIR193BHG]] | +0.62 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[TBC1D20]] | +0.62 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[FBXO42]] | +0.61 | +0.51 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF10]] | -0.60 | -0.46 / -0.64 | both halves | 3e-05 |  |
| [[XRCC5]] | -0.59 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[UTP20]] | -0.59 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[SMARCB1]] | -0.58 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[PBRM1]] | -0.58 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[TFAM]] | -0.58 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[ZNF280D]] | -0.57 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[ZNF644]] | -0.56 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[PARVA]] | -0.56 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[ZMYND11]] | -0.56 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[INTS7]] | -0.56 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[EXOSC10]] | -0.56 | -0.39 / -0.56 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRTN]] | C | NRTN activity lowers RAB11FIP5's level | lines that do not express NRTN (4) vs lines expressing it (46) | 1.77× higher at baseline in the lines without NRTN | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, ATP11A, BRME1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 180]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.5, -17.1); signed map (-31.7, 17.9). **Vector** length 120, 34.5% of its response variance represented; |z| ≥ 3 in 893 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +7.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.8 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.6 | +5.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.0 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.1 | +3.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +4.0 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.1 | -8.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.0 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.5 | -3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -0.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.8 | -3.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.7 | -1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | RAB11 family interacting protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.2 — chr2:73,073,382-73,156,721 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GAF1, KIAA0857, RIP11, pp75 |
| Gene groups (HGNC) | C2 domain containing; RAB11 binding domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXF6](https://www.uniprot.org/uniprotkb/Q9BXF6) (Rab11 family-interacting protein 5):

> Rab effector involved in protein trafficking from apical recycling endosomes to the apical plasma membrane. Involved in insulin granule exocytosis. May regulate V-ATPase intracellular transport in response to extracellular acidosis.

**Summary**, from NCBI Gene [26056](https://www.ncbi.nlm.nih.gov/gene/26056):

> Enables gamma-tubulin binding activity. Involved in cellular response to acidic pH; negative regulation of adiponectin secretion; and regulation of protein localization to cell surface. Located in mitochondrial outer membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24845](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24845) · Entrez [26056](https://www.ncbi.nlm.nih.gov/gene/26056) · UniProt [Q9BXF6](https://www.uniprot.org/uniprotkb/Q9BXF6) · Ensembl [ENSG00000135631](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135631)

## Data

Gene col 5733: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5733); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5733, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5733]; `tensor/DDL_lfc|DDL_z.npy` [5733]; `embed/gene_vectors.npy` [5733]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5733 or target_col == 5733). Every well: [[RAB11FIP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB11FIP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
