---
symbol: "LRRC37A2"
type: "gene"
col: 14167
ensembl_id: "ENSG00000238083"
name: "leucine rich repeat containing 37 member A2"
location: "17q21.31"
module: 28
arm: "+"
pooled_cpm: 10.82
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# LRRC37A2

*leucine rich repeat containing 37 member A2* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.63× (z +11.2, q 3e-26, up in 31 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.536× (z -10.2, q 1e-21, down in 34 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP350]] (+0.73, fdr 7e-06), [[BPTF]] (+0.70, fdr 7e-06), [[ZNF638]] (+0.69, fdr 1e-05); moves opposite to [[ZNF512]] (-0.67, fdr 7e-06), [[C1orf216]] (-0.67, fdr 1e-05), [[PMPCA]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14167.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +11.2 | 3e-26 | 31/46 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +5.8 | 1e-06 | 19/46 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.4 | 0.002 | 18/43 (PANC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.31×** | +4.3 | 0.003 | 19/46 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.7 | 0.024 | 1/48 (NCI-H1792) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.028 | 11/46 (SHP-77, C-33 A, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.077 | 7/47 (J82, A-172, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.083 | 6/48 (HEC-1-A, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.18× | +3.0 | 0.17 | 5/48 (A-172, KATO III, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14167.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.536×** | -10.2 | 1e-21 | 34/46 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.753×** | -4.7 | 9e-04 | 18/36 (NCI-H460, CFPAC-1, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.757×** | -4.4 | 0.002 | 19/40 (KATO III, H4, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -4.2 | 0.004 | 17/48 (C32, SHP-77, …) | top dose only | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.780×** | -4.1 | 0.005 | 16/41 (Panc 03.27, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.799×** | -3.7 | 0.021 | 10/47 (SNU-423, C-33 A, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.790×** | -3.6 | 0.025 | 17/44 (SNU-423, J82, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.806×** | -3.5 | 0.028 | 15/47 (NCI-H1573, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.796×** | -3.5 | 0.029 | 11/26 (HOP62, A549, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.810×** | -3.5 | 0.029 | 16/47 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Flutamide (drug)]] 0.5 µM |  | **0.813×** | -3.4 | 0.035 | 11/46 (RKO, SK-MEL-2, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.678×** | -3.3 | 0.041 | 7/18 (HOP62, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Saquinavir (drug)]] 0.5 µM |  | 0.821× | -3.0 | 0.11 | 10/43 (SW48, Panc 03.27, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14167. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0709× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[KATO III (line)]] | alt | 14.3 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.189× (z -10.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.195× (z -9.0) |
| [[SW480 (line)]] | alt | 14.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.294× (z -10.4) |
| [[A549 (line)]] | wt | 14.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[C32 (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.219× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HOP62 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0679× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[PANC-1 (line)]] | alt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.271× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 8.51 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.100× (z -10.8) |
| [[A-172 (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14167), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP350]] | +0.73 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[BPTF]] | +0.70 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[ZNF638]] | +0.69 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[ANKRD26]] | +0.69 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[ZC3H6]] | +0.66 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[SPG11]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[HMGXB4]] | +0.62 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[NIPBL]] | +0.61 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[TRIP11]] | +0.60 | +0.70 / +0.43 | both halves | 3e-05 |  |
| [[ASH1L]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[RSF1]] | +0.59 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[DARS1]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF512]] | -0.67 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[C1orf216]] | -0.67 | -0.51 / -0.79 | both halves | 1e-05 |  |
| [[PMPCA]] | -0.62 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[SDHAP4]] | -0.61 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[CDK9]] | -0.59 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[FBXW2]] | -0.58 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[SNHG21]] | -0.58 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[ABHD17A]] | -0.57 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[CTC-338M12.4]] | -0.56 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[SEPTIN7P13]] | -0.55 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[MAT2A]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[CPSF4]] | -0.54 | -0.53 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.546). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-25.3, 7.3); signed map (6.1, -16.3). **Vector** length 58.4, 7.60% of its response variance represented; |z| ≥ 3 in 905 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +11.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.8 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.0 | +4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +0.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.1 | +3.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.1 | +1.9 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.0 | +1.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.2 | -10.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -3.5 | -3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | -3.2 | -4.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.3 | -0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.4 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 37 member A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:46,511,508-46,556,910 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ45049 |
| Matched by | ensembl_id |

UniProt [A6NM11](https://www.uniprot.org/uniprotkb/A6NM11) carries no function annotation.

**Summary**, from NCBI Gene [474170](https://www.ncbi.nlm.nih.gov/gene/474170):

> Predicted to enable ATP binding activity; ATP hydrolysis activity; and metal ion binding activity. Predicted to be involved in SNARE complex disassembly and protein transport. Predicted to be located in cytoplasm and membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:32404](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32404) · Entrez [474170](https://www.ncbi.nlm.nih.gov/gene/474170) · UniProt [A6NM11](https://www.uniprot.org/uniprotkb/A6NM11) · Ensembl [ENSG00000238083](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000238083)

## Data

Gene col 14167: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14167); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14167, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14167]; `tensor/DDL_lfc|DDL_z.npy` [14167]; `embed/gene_vectors.npy` [14167]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14167 or target_col == 14167). Every well: [[LRRC37A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC37A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
