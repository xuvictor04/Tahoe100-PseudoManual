---
symbol: "CNTN4"
type: "gene"
col: 6904
ensembl_id: "ENSG00000144619"
name: "contactin 4"
location: "3p26.3-p26.2"
module: 166
arm: "+"
pooled_cpm: 4.51
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/166"]
generated_by: "tahoemap"
---

# CNTN4

*contactin 4* — 3p26.3-p26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.57× (z +20.7, q 0e+00, up in 26 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.659× (z -4.8, q 0.001, down in 14 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (C32 0.0753×, H4 0.0628×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (H4 0.147×, CHP-212 0.256×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (CHP-212 0.0210×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.0867×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (H4 0.0559×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SORCS1]] (+0.81, fdr 7e-06), [[CNBD1]] (+0.78, fdr 7e-06), [[DCC]] (+0.76, fdr 7e-06).
> It is in [[Module 166]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6904.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.57×** | +20.7 | 0e+00 | 26/35 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.59×** | +14.1 | 1e-42 | 1/5 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.34×** | +13.8 | 3e-41 | 29/45 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.20×** | +13.4 | 2e-38 | 11/18 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.18×** | +12.6 | 2e-34 | 24/37 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.99×** | +12.6 | 3e-34 | 25/41 (HT-29, A498, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.87×** | +11.2 | 4e-27 | 3/7 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.44×** | +10.3 | 8e-23 | 24/39 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.89×** | +7.3 | 2e-11 | 6/19 (NCI-H2347, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.89×** | +7.3 | 2e-11 | 18/43 (HEC-1-A, BT-474, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +6.4 | 7e-09 | 14/36 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +5.3 | 4e-06 | 5/30 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.45×** | +4.2 | 1e-03 | 17/45 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.42×** | +4.0 | 0.003 | 13/44 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.41×** | +3.9 | 0.003 | 11/44 (HS-578T, NCI-H23, …) | rises with dose |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.008 | 4/38 (NCI-H460, J82, …) | top dose only |  |
| [[Imiquimod (maleate) (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.022 | 4/41 (A549, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.34×** | +3.3 | 0.026 | 5/42 (C32, SW480, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.042 | 0/39 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +3.2 | 0.044 | 12/44 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.047 | 5/34 (SW1417, SHP-77, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.048 | 3/40 (NCI-H2347, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6904.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (C32 0.0753×, H4 0.0628×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (H4 0.147×, CHP-212 0.256×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (CHP-212 0.0210×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.0867×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (H4 0.0559×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.659×** | -4.8 | 0.001 | 14/43 (H4, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.918× | -3.4 | 0.23 | 11/47 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Asciminib (drug)]] 0.05 µM |  | 0.764× | -3.1 | 0.39 | 9/44 (RPMI-7951, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6904. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 247 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0210× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0867× (z -15.8) |
| [[H4 (line)]] | wt | 27.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0559× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 3.16 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 11.8× (z +12.2) | — |
| [[SW480 (line)]] | alt | 2.36 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 16.9× (z +15.4) | — |
| [[C32 (line)]] | wt | 29.1 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.93× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.0753× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H23 (line)]] | alt | 5.25 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 8.92× (z +9.7) | [[Peretinoin (drug)]] 0.5 µM 0.0676× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 2.76 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 9.27× (z +11.4) | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0929× (z -8.6) |
| [[A549 (line)]] | wt | 1.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 7.24 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.62× (z +10.9) | — |
| [[HEC-1-A (line)]] | alt | 9.17 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.85× (z +10.2) | — |
| [[LoVo (line)]] | wt | 2.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.89× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 4.18 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.20× (z +10.5) | — |
| [[A-172 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6904), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SORCS1]] | +0.81 | +0.68 / +0.85 | both halves | 7e-06 | STRING 550 |
| [[CNBD1]] | +0.78 | +0.68 / +0.81 | both halves | 7e-06 |  |
| [[DCC]] | +0.76 | +0.64 / +0.77 | both halves | 7e-06 | same gene group |
| [[CNTN5]] | +0.74 | +0.72 / +0.68 | both halves | 7e-06 | same gene group; pathway: Post-translational modification: synthesis of GPI-anchored proteins; STRING 441 |
| [[THSD7B]] | +0.74 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.74 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[HPSE2]] | +0.74 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[OBI1-AS1]] | +0.74 | +0.61 / +0.80 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.74 | +0.65 / +0.78 | both halves | 7e-06 | same gene group |
| [[COL25A1]] | +0.73 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[ATP8A2]] | +0.73 | +0.63 / +0.78 | both halves | 7e-06 |  |
| [[ST8SIA1]] | +0.73 | +0.65 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 166]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.815). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.7, 28.7); signed map (32.7, 15.7). **Vector** length 62.0, 9.24% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.0 | +13.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +20.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.8 | +13.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.6 | +10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +14.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.9 | +12.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +1.5 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.9 | -3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -0.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.9 | -1.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -0.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -0.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | contactin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p26.3-p26.2 — chr3:2,098,813-3,057,959 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BIG-2 |
| Gene groups (HGNC) | I-set domain containing; Contactins |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWV2](https://www.uniprot.org/uniprotkb/Q8IWV2) (Contactin-4):

> Contactins mediate cell surface interactions during nervous system development. Has some neurite outgrowth-promoting activity. May be involved in synaptogenesis.

**Summary**, from NCBI Gene [152330](https://www.ncbi.nlm.nih.gov/gene/152330):

> This gene encodes a member of the contactin family of immunoglobulins. Contactins are axon-associated cell adhesion molecules that function in neuronal network formation and plasticity. The encoded protein is a glycosylphosphatidylinositol-anchored neuronal membrane protein that may play a role in the formation of axon connections in the developing nervous system. Deletion or mutation of this gene may play a role in 3p deletion syndrome and autism spectrum disorders. Alternative splicing …

**Accessions** — [HGNC:2174](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2174) · Entrez [152330](https://www.ncbi.nlm.nih.gov/gene/152330) · UniProt [Q8IWV2](https://www.uniprot.org/uniprotkb/Q8IWV2) · Ensembl [ENSG00000144619](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144619)

## Data

Gene col 6904: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6904); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6904, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6904]; `tensor/DDL_lfc|DDL_z.npy` [6904]; `embed/gene_vectors.npy` [6904]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6904 or target_col == 6904). Every well: [[CNTN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNTN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
