---
symbol: "STK19"
type: "gene"
col: 12854
ensembl_id: "ENSG00000204344"
name: "winged helix repair factor 1"
location: "6p21.33"
module: 41
arm: "+"
pooled_cpm: 12.91
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# STK19

*winged helix repair factor 1* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.37× (z +6.7, q 1e-08, up in 25 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 3.55×).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.623× (z -7.0, q 2e-09, down in 22 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC9]] (+0.78, fdr 7e-06), [[CWC25]] (+0.68, fdr 7e-06), [[TRIM39]] (+0.66, fdr 7e-06); moves opposite to [[NCKAP1]] (-0.52, fdr 4e-05), [[NAE1]] (-0.51, fdr 4e-05), [[GLO1]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12854.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 3.55×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +6.7 | 1e-08 | 25/47 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +6.6 | 2e-08 | 5/48 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.72×** | +4.3 | 0.003 | 17/48 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | 1.18× | +3.5 | 0.059 | 15/44 (HEC-1-A, HCT15, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | 1.24× | +3.2 | 0.15 | 18/48 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12854.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.623×** | -7.0 | 2e-09 | 22/46 (NCI-H2030, H4, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.671×** | -5.9 | 1e-06 | 16/27 (HS-578T, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.720×** | -5.0 | 8e-05 | 17/47 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.717×** | -4.9 | 1e-04 | 18/46 (NCI-H1792, NCI-H2030, …) | top dose only |  |
| [[Azithromycin (hydrate) (drug)]] 0.5 µM |  | **0.734×** | -4.8 | 2e-04 | 18/47 (NCI-H460, HOP62, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.672×** | -4.4 | 0.001 | 15/44 (Hs 766T, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.820×** | -4.3 | 0.001 | 14/48 (HOP62, NCI-H460, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.830×** | -4.1 | 0.003 | 10/48 (HT-29, CFPAC-1, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **0.765×** | -4.0 | 0.005 | 17/42 (HepG2/C3A, RKO, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.715×** | -3.7 | 0.014 | 12/45 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib (drug)]] 0.05 µM |  | **0.792×** | -3.4 | 0.037 | 12/46 (SW48, A498, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.808×** | -3.3 | 0.048 | 17/36 (NCI-H1792, RPMI-7951, …) | rises with dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.810×** | -3.2 | 0.051 | 15/47 (HS-578T, H4, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -3.2 | 0.062 | 12/48 (SK-MEL-2, HOP62, …) | top dose only | low cells (technical?) |
| [[Peretinoin (drug)]] 5 µM |  | **0.808×** | -3.1 | 0.062 | 9/46 (NCI-H1792, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.810×** | -3.1 | 0.062 | 20/47 (RPMI-7951, H4, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.787×** | -3.1 | 0.070 | 15/43 (SW48, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **0.761×** | -3.0 | 0.082 | 7/44 (NCI-H2030, HS-578T, …) | all doses, flat | low cells (technical?); noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12854. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 10.6 | 0 | 2 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0901× (z -8.9) |
| [[H4 (line)]] | wt | 23.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -8.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 13.2 | 0 | 2 (1 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.146× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 21.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -9.7) |
| [[A498 (line)]] | wt | 14.5 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.290× (z -8.5) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 19.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0878× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~20% of this change |
| [[Hs 766T (line)]] | wt | 13.1 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0917× (z -12.7) |
| [[HS-578T (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0464× (z -18.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.195× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~20% of this change |
| [[LS 180 (line)]] | wt | 7.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.112× (z -11.9) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0924× (z -9.3) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[RKO (line)]] | wt | 8.68 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.104× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~20% of this change |
| [[RPMI-7951 (line)]] | alt | 18.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -9.8) |
| [[SNU-1 (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0745× (z -9.2) ⚠ cell-cycle shift, explains ~15% of this change |
| [[SW1417 (line)]] | alt | 7.83 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0924× (z -11.3) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12854), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC9]] | +0.78 | +0.73 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[CWC25]] | +0.68 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[TRIM39]] | +0.66 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[FOXRED1]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[EDC3]] | +0.62 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[COQ10B]] | +0.60 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[ELP5]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[C5AR1]] | +0.59 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ARF4]] | +0.59 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[RNF213-AS1]] | +0.59 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[BBOF1]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[CHRNE]] | +0.58 | +0.56 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCKAP1]] | -0.52 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[NAE1]] | -0.51 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[GLO1]] | -0.50 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[CDYL]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[HACD3]] | -0.49 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[TRIM33]] | -0.48 | -0.50 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.582). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (8.9, -37.1); signed map (-7.7, -2.5). **Vector** length 74.4, 12.8% of its response variance represented; |z| ≥ 3 in 868 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +6.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.0 | +4.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +1.9 | +6.6 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.8 | +2.2 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.3 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | +2.3 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.1 | +1.9 |
|  | [[Cinacalcet (drug)]] 5 µM |  | +1.1 | +0.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -4.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -7.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -3.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | -3.0 | -4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.9 | -2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | winged helix repair factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,971,091-31,982,821 (+) |
| Ensembl biotype | protein_coding |
| Also known as | G11, RP1, D6S60, TWH19; previously STK19 |
| Matched by | ensembl_id |

**Function**, from UniProt [P49842](https://www.uniprot.org/uniprotkb/P49842) (Winged helix repair factor 1):

> DNA-binding protein which is required for efficient transcription-coupled nucleotide excision repair (TC-NER). Acts as part of a TC-NER complex which assembles and interacts with RNA polymerase II (RNAPII) when it stalls at DNA lesions. TC-NER complex subunit UVSSA binds to the GTF2H1/p62 subunit of the TFIIH transcription factor complex, tethering TFIIH to the TC-NER complex. WHR1/STK19 then interacts with the XPD helicase subunit of TFIIH which guides TFIIH to DNA downstream of the stalled …

**Summary**, from NCBI Gene [8859](https://www.ncbi.nlm.nih.gov/gene/8859):

> This gene encodes a serine/threonine kinase which localizes predominantly to the nucleus. Its specific function is unknown; it is possible that phosphorylation of this protein is involved in transcriptional regulation. This gene localizes to the major histocompatibility complex (MHC) class III region on chromosome 6 and expresses two transcript variants. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11398](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11398) · Entrez [8859](https://www.ncbi.nlm.nih.gov/gene/8859) · UniProt [P49842](https://www.uniprot.org/uniprotkb/P49842) · Ensembl [ENSG00000204344](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204344)

## Data

Gene col 12854: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12854); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12854, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12854]; `tensor/DDL_lfc|DDL_z.npy` [12854]; `embed/gene_vectors.npy` [12854]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12854 or target_col == 12854). Every well: [[STK19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STK19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
