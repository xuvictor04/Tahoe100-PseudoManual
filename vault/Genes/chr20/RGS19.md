---
symbol: "RGS19"
type: "gene"
col: 10148
ensembl_id: "ENSG00000171700"
name: "regulator of G protein signaling 19"
location: "20q13.33"
module: 23
arm: "-"
pooled_cpm: 4.35
n_lines_expressing: 48
n_dd_up: 5
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# RGS19

*regulator of G protein signaling 19* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.33× (z +7.6, q 1e-11, up in 5 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM: 1.55× (z +4.1, q 0.006, up in 7 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.266× (z -17.4, q 0e+00, down in 35 of 37 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPUSD1]] (+0.66, fdr 1e-05), [[UBL4A]] (+0.63, fdr 9e-06), [[TMCO6]] (+0.61, fdr 3e-05); moves opposite to [[TMEM91]] (-0.64, fdr 2e-05), [[ZSCAN16-AS1]] (-0.64, fdr 4e-05), [[COPZ1]] (-0.59, fdr 3e-05).
> It sits in the **-** arm of [[Module 023]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10148.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.33×** | +7.6 | 1e-11 | 5/7 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +5.9 | 1e-06 | 14/20 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.74×** | +5.2 | 4e-05 | 6/20 (A-427, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.55×** | +4.1 | 0.006 | 7/33 (SW1417, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.080 | 4/44 (A-427, BT-474, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10148.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.266×** | -17.4 | 0e+00 | 35/37 (NCI-H2030, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.297×** | -11.3 | 3e-27 | 37/45 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.318×** | -10.3 | 2e-22 | 35/41 (NCI-H23, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.484×** | -9.6 | 2e-19 | 30/34 (Panc 03.27, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.388×** | -8.8 | 1e-16 | 33/42 (BT-474, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.390×** | -8.8 | 2e-16 | 27/42 (Hs 766T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.421×** | -8.1 | 6e-14 | 26/35 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.475×** | -6.9 | 3e-10 | 20/32 (NCI-H23, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.374×** | -4.8 | 1e-04 | 20/33 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.396×** | -4.5 | 4e-04 | 21/39 (Panc 03.27, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.681×** | -3.6 | 0.018 | 8/44 (Panc 03.27, HOP62, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.689×** | -3.5 | 0.026 | 10/45 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.691×** | -3.3 | 0.042 | 11/35 (NCI-H23, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM |  | **0.718×** | -3.1 | 0.084 | 8/40 (HOP62, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10148. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 5.76 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 6.37 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -12.0) |
| [[A-172 (line)]] | wt | 5.77 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -13.0) |
| [[BT-474 (line)]] | alt | 4.58 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0502× (z -12.7) |
| [[HT-29 (line)]] | alt | 6.35 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0833× (z -14.3) |
| [[KATO III (line)]] | alt | 6.96 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 5.35 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0941× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 10.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0647× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.0807× (z -11.5) |
| [[PANC-1 (line)]] | alt | 5.35 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0671× (z -13.4) |
| [[SW480 (line)]] | alt | 6.12 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 3.46 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0298× (z -10.5) |
| [[C-33 A (line)]] | alt | 8.23 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 3.71 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0775× (z -12.2) |
| [[HOP62 (line)]] | alt | 2.09 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0902× (z -9.6) |
| [[HS-578T (line)]] | alt | 2.81 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0379× (z -9.3) |
| [[LoVo (line)]] | wt | 2.78 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0784× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 5.05 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0933× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 2.41 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0874× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 7.80 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0514× (z -18.9) |
| [[NCI-H460 (line)]] | wt | 2.17 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -9.8) |
| [[SW1417 (line)]] | alt | 7.95 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -10.2) |
| [[A-427 (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.304 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.968 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10148), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPUSD1]] | +0.66 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[UBL4A]] | +0.63 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[TMCO6]] | +0.61 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[CPTP]] | +0.61 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[CBR1]] | +0.60 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[GPRIN1]] | +0.60 | +0.53 / +0.35 | both halves | 1e-04 |  |
| [[USB1]] | +0.59 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[ADAMTSL5]] | +0.59 | +0.64 / +0.38 | both halves | 6e-05 |  |
| [[HYAL2]] | +0.58 | +0.63 / +0.34 | both halves | 1e-04 |  |
| [[TWF2]] | +0.58 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[BOK]] | +0.57 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[RRP1B]] | +0.57 | +0.38 / +0.46 | both halves | 6e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM91]] | -0.64 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[ZSCAN16-AS1]] | -0.64 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[COPZ1]] | -0.59 | -0.52 / -0.44 | both halves | 3e-05 | same gene group |
| [[GTF2IRD2]] | -0.59 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[ETFRF1]] | -0.59 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[MFF-DT]] | -0.59 | -0.51 / -0.22 | both halves | 6e-04 |  |
| [[HEXIM2-AS1]] | -0.59 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[UGDH-AS1]] | -0.58 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[ENTPD3-AS1]] | -0.58 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[LINC00938]] | -0.57 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[DICER1-AS1]] | -0.56 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[NDUFA6-DT]] | -0.56 | -0.49 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.603). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-8.1, 28.0); signed map (-31.6, -33.7). **Vector** length 50.5, 6.92% of its response variance represented; |z| ≥ 3 in 898 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.8 | -0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | -2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | -1.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | -2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | -0.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.2 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.1 | +0.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -17.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.3 | -8.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -11.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.9 | -8.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | -1.1 | -1.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.1 | -0.4 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | regulator of G protein signaling 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:64,073,181-64,079,988 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GAIP, RGSGAIP |
| Gene groups (HGNC) | Regulators of G-protein signaling; MicroRNA protein coding host genes |
| Reactome | 5 pathways, smallest: G alpha (z) signalling events; G alpha (q) signalling events; G alpha (i) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P49795](https://www.uniprot.org/uniprotkb/P49795) (Regulator of G protein signaling 19):

> Inhibits signal transduction by increasing the GTPase activity of G protein alpha subunits thereby driving them into their inactive GDP-bound form. Binds to G-alpha subfamily 1 members, with the order G(i)a3 > G(i)a1 > G(o)a >> G(z)a/G(i)a2. Activity on G(z)-alpha is inhibited by phosphorylation and palmitoylation of the G protein.

**Summary**, from NCBI Gene [10287](https://www.ncbi.nlm.nih.gov/gene/10287):

> G proteins mediate a number of cellular processes. The protein encoded by this gene belongs to the RGS (regulators of G-protein signaling) family and specifically interacts with G protein, GAI3. This protein is a guanosine triphosphatase-activating protein that functions to down-regulate Galpha i/Galpha q-linked signaling. Alternatively spliced transcript variants encoding the same protein isoform have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:13735](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13735) · Entrez [10287](https://www.ncbi.nlm.nih.gov/gene/10287) · UniProt [P49795](https://www.uniprot.org/uniprotkb/P49795) · Ensembl [ENSG00000171700](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171700)

## Data

Gene col 10148: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10148); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10148, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10148]; `tensor/DDL_lfc|DDL_z.npy` [10148]; `embed/gene_vectors.npy` [10148]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10148 or target_col == 10148). Every well: [[RGS19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RGS19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
