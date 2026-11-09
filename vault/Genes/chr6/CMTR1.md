---
symbol: "CMTR1"
type: "gene"
col: 5984
ensembl_id: "ENSG00000137200"
name: "cap methyltransferase 1"
location: "6p21.2"
module: 32
arm: "+"
pooled_cpm: 42.63
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 25
direction_downstream: 12
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# CMTR1

*cap methyltransferase 1* — 6p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.40× (z +6.8, q 8e-09, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.585× (z -10.9, q 5e-25, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAR]] (+0.82, fdr 7e-06), [[SLC15A3]] (+0.80, fdr 7e-06), [[IFI35]] (+0.79, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[OAS2]] → it (grade B ⚠); 12 go from it, the strongest it → [[SAMHD1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5984.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +6.8 | 8e-09 | 28/48 (NCI-H2347, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +4.6 | 9e-04 | 21/48 (HS-578T, NCI-H2347, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.25×** | +4.6 | 1e-03 | 22/48 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 0.001 | 21/48 (Panc 03.27, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.22×** | +4.0 | 0.006 | 20/48 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.23×** | +4.0 | 0.007 | 17/48 (PANC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.21×** | +3.8 | 0.010 | 10/48 (AsPC-1, SHP-77, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.010 | 14/47 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.22×** | +3.8 | 0.010 | 17/48 (CFPAC-1, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | **1.21×** | +3.7 | 0.010 | 15/48 (AsPC-1, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.016 | 18/47 (NCI-H2347, AsPC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.19× | +3.6 | 0.016 | 12/48 (AsPC-1, SNU-1, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.6 | 0.016 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.14× | +3.5 | 0.016 | 12/48 (Hs 766T, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.15× | +3.5 | 0.020 | 13/48 (AsPC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.13× | +3.4 | 0.021 | 10/48 (CFPAC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.15× | +3.4 | 0.021 | 17/48 (Hs 766T, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | 1.13× | +3.4 | 0.023 | 10/48 (Hs 766T, MIA PaCa-2, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +3.4 | 0.023 | 17/47 (LoVo, Hs 766T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.039 | 19/47 (HS-578T, A-427, …) | all doses, flat | low cells (technical?) |
| [[Binimetinib (drug)]] 5 µM |  | 1.16× | +2.9 | 0.094 | 13/48 (CFPAC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5984.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.585×** | -10.9 | 5e-25 | 41/48 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.660×** | -8.2 | 6e-14 | 32/47 (C-33 A, A-172, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.754×** | -8.2 | 6e-14 | 29/48 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.780×** | -7.2 | 1e-10 | 30/48 (A549, NCI-H23, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.712×** | -6.9 | 4e-10 | 30/48 (RPMI-7951, A498, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.745×** | -6.0 | 2e-07 | 28/48 (LoVo, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.781×** | -5.1 | 3e-05 | 23/47 (NCI-H2347, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.845× | -4.9 | 7e-05 | 20/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.655×** | -4.5 | 4e-04 | 22/48 (CFPAC-1, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.813×** | -4.2 | 0.001 | 21/48 (SW 1088, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.879× | -3.8 | 0.008 | 18/48 (NCI-H23, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Tofacitinib (drug)]] 0.05 µM |  | **0.833×** | -3.7 | 0.008 | 18/48 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.834× | -3.7 | 0.009 | 13/47 (H4, C32, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.831×** | -3.6 | 0.013 | 20/48 (MIA PaCa-2, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | 0.850× | -3.3 | 0.032 | 14/48 (RPMI-7951, NCI-H1573, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.856× | -3.2 | 0.042 | 17/48 (MIA PaCa-2, COLO 205, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.854× | -3.1 | 0.053 | 15/47 (NCI-H23, H4, …) | rises with dose |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.813×** | -3.0 | 0.066 | 8/48 (C32, SHP-77, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5984. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 63.9 | 2 (1 ⚠) | 5 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 2.35× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.23× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.367× (z -11.0) |
| [[A549 (line)]] | wt | 45.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0852× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.484× (z -8.8) |
| [[LoVo (line)]] | wt | 49.7 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.272× (z -12.7) |
| [[RKO (line)]] | wt | 57.9 | 0 | 3 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 50.3 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.338× (z -10.1) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.388× (z -9.2) |
| [[AN3 CA (line)]] | alt | 65.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 73.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -11.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.439× (z -8.7) |
| [[SW1417 (line)]] | alt | 43.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.342× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 69.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.205× (z -11.2) ⚠ toxic |
| [[C32 (line)]] | wt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.345× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 38.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -9.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 31.0 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.250× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.356× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 51.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.337× (z -10.3) |
| [[J82 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.182× (z -8.8) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 35.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 22.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 69.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.363× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 78.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.398× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 60.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.373× (z -8.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 43.7 | 0 | 1 | — | [[IQ 1 (drug)]] 5 µM 0.0892× (z -9.7) |
| [[SNU-1 (line)]] | wt | 38.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -9.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 31.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5984), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAR]] | +0.82 | +0.75 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 415 |
| [[SLC15A3]] | +0.80 | +0.74 / +0.83 | both halves | 7e-06 |  |
| [[IFI35]] | +0.79 | +0.76 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[OAS3]] | +0.78 | +0.70 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[PARP9]] | +0.78 | +0.68 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[SHFL]] | +0.77 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[OAS2]] | +0.77 | +0.69 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[PML]] | +0.77 | +0.70 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[SAMHD1]] | +0.77 | +0.69 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[CMPK2]] | +0.77 | +0.67 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[TRIM14]] | +0.77 | +0.66 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[SAMD9L]] | +0.77 | +0.69 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 3, C 22. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS2]] | B | OAS2 activity strengthens CMTR1's drug response | lines that do not express OAS2 (14) vs lines expressing it (34) | the lines without OAS2 respond 0.45× as strongly (z diff +1.18); strongest at Auranofin 5 µM: 0.66x vs 0.52x (z diff +2.8) | 0.034 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1; target measured in part of the lines; artifact flags |
| [[GMPR]] | B | GMPR activity raises CMTR1's level | lines that do not express GMPR (14) vs lines expressing it (36) | 1.30× lower at baseline in the lines without GMPR | 0.040 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[IFI6]] | B | IFI6 activity strengthens CMTR1's drug response | lines that do not express IFI6 (13) vs lines expressing it (35) | the lines without IFI6 respond 0.34× as strongly (z diff +1.62); strongest at Dinaciclib 0.5 µM: 0.91x vs 0.69x (z diff +2.8) | 0.093 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[EIF2AK2]] | C | EIF2AK2's natural level strengthens CMTR1's drug response | EIF2AK2's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.81, reverse +0.42; direction not clear | 1e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[STAT1]] | C | STAT1's natural level strengthens CMTR1's drug response | STAT1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.80, reverse +0.58; direction not clear | 1e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ADAR]] | C | ADAR's natural level strengthens CMTR1's drug response | ADAR's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.74, reverse +0.66; direction not clear | 0.003 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PML]] | C | PML's natural level strengthens CMTR1's drug response | PML's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.74, reverse +0.57; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP12]] | C | PARP12's natural level strengthens CMTR1's drug response | PARP12's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.74, reverse +0.69; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[LAP3]] | C | LAP3's natural level strengthens CMTR1's drug response | LAP3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.72, reverse -0.14; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT5]] | C | IFIT5's natural level strengthens CMTR1's drug response | IFIT5's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.70; direction not clear | 0.007 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PNPT1]] | C | PNPT1's natural level strengthens CMTR1's drug response | PNPT1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.60; direction not clear | 0.009 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[USP18]] | C | USP18's natural level strengthens CMTR1's drug response | USP18's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.73; direction not clear | 0.011 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMHD1]] | C | CMTR1's natural level strengthens SAMHD1's drug response | CMTR1's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.78, reverse +0.63; direction not clear | 0.002 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IRF9]] | C | CMTR1's natural level strengthens IRF9's drug response | CMTR1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.74, reverse +0.67; direction not clear | 0.002 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[USP18]] | C | CMTR1's natural level strengthens USP18's drug response | CMTR1's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.73; direction not clear | 0.011 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT5]] | C | CMTR1's natural level strengthens IFIT5's drug response | CMTR1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.72; direction not clear | 0.014 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT1]] | C | CMTR1's natural level strengthens IFIT1's drug response | CMTR1's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.41; direction not clear | 0.014 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP12]] | C | CMTR1's natural level strengthens PARP12's drug response | CMTR1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.74; direction not clear | 0.019 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ADAR]] | C | CMTR1's natural level strengthens ADAR's drug response | CMTR1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.74; direction not clear | 0.035 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HELZ2]] | C | CMTR1's natural level strengthens HELZ2's drug response | CMTR1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.68; direction not clear | 0.040 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP14]] | C | CMTR1's natural level strengthens PARP14's drug response | CMTR1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.65; direction not clear | 0.054 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ISG15]] | C | CMTR1's natural level strengthens ISG15's drug response | CMTR1's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.46; direction not clear | 0.075 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[IFIT3]] | C | CMTR1's natural level strengthens IFIT3's drug response | CMTR1's natural level across 41 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.35; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP10]] | C | CMTR1's natural level strengthens PARP10's drug response | CMTR1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.71; direction not clear | 0.085 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.775). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.4, 54.8); signed map (65.5, 32.9). **Vector** length 115, 29.7% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.71 to 23); *Interferon Signaling* (reactome, mean cos +0.68 to 45); *Interferon alpha/beta signaling* (reactome, mean cos +0.69 to 27).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.0 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.5 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.0 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.4 | +4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.3 | +3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.1 | +3.8 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +2.9 | +4.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.9 | +3.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.0 | -10.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.3 | -7.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.6 | -8.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.9 | -8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.8 | -4.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -5.4 | -6.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -5.2 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | cap methyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.2 — chr6:37,433,219-37,482,827 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MTr1, ISG95; previously KIAA0082, FTSJD2 |
| Gene groups (HGNC) | G-patch domain containing; 7BS 2'O-ribose DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N1G2](https://www.uniprot.org/uniprotkb/Q8N1G2) (Cap-specific mRNA):

> S-adenosyl-L-methionine-dependent methyltransferase that mediates mRNA cap1 2'-O-ribose methylation to the 5'-cap structure of mRNAs. Methylates the ribose of the first nucleotide of a m(7)GpppG-capped mRNA and small nuclear RNA (snRNA) to produce m(7)GpppRm (cap1). Displays a preference for cap0 transcripts. Cap1 modification is linked to higher levels of translation. May be involved in the interferon response pathway.

**Summary**, from NCBI Gene [23070](https://www.ncbi.nlm.nih.gov/gene/23070):

> Enables methyltransferase cap1 activity. Involved in 7-methylguanosine mRNA capping. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21077](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21077) · Entrez [23070](https://www.ncbi.nlm.nih.gov/gene/23070) · UniProt [Q8N1G2](https://www.uniprot.org/uniprotkb/Q8N1G2) · Ensembl [ENSG00000137200](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137200)

## Data

Gene col 5984: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5984); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5984, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5984]; `tensor/DDL_lfc|DDL_z.npy` [5984]; `embed/gene_vectors.npy` [5984]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5984 or target_col == 5984). Every well: [[CMTR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CMTR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
