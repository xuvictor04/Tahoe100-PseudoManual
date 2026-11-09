---
symbol: "LSM3"
type: "gene"
col: 10014
ensembl_id: "ENSG00000170860"
name: "LSM3 homolog, U6 small nuclear RNA and mRNA degradation associated"
location: "3p25.1"
module: 71
arm: "+"
pooled_cpm: 34.5
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/071", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# LSM3

*LSM3 homolog, U6 small nuclear RNA and mRNA degradation associated* — 3p25.1

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.18× (z +10.4, q 1e-22, up in 44 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (NCI-H460 5.53×, A549 5.17×, A-427 4.30×, SW480 3.77×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 3.60×, PANC-1 3.51×, SW480 3.41×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.287×); [[Ivabradine (hydrochloride) (drug)]] 0.5 µM in 1 line (SW 1271 0.0690×; ⚠ transcription drop; unreliable plate only); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (AN3 CA 0.131×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPA3]] (+0.64, fdr 7e-06), [[MTBP]] (+0.62, fdr 1e-05), [[TPRKB]] (+0.61, fdr 7e-06); moves opposite to [[KTN1-AS1]] (-0.48, fdr 4e-05), [[PRRC2B]] (-0.47, fdr 4e-05), [[CDV3]] (-0.46, fdr 7e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10014.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (NCI-H460 5.53×, A549 5.17×, A-427 4.30×, SW480 3.77×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 3.60×, PANC-1 3.51×, SW480 3.41×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.18×** | +10.4 | 1e-22 | 44/45 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.69×** | +9.1 | 3e-17 | 37/38 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.09×** | +6.2 | 9e-08 | 33/42 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.68×** | +5.0 | 1e-04 | 34/47 (PANC-1, KATO III, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.61×** | +4.7 | 3e-04 | 36/48 (PANC-1, LoVo, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | **1.59×** | +4.4 | 9e-04 | 32/46 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +4.4 | 1e-03 | 3/48 (SW48, SNU-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.5 | 0.040 | 24/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.42× | +3.1 | 0.11 | 21/48 (NCI-H1573, NCI-H460, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.38× | +3.0 | 0.13 | 26/48 (SK-MEL-2, SW480, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10014.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.287×); [[Ivabradine (hydrochloride) (drug)]] 0.5 µM in 1 line (SW 1271 0.0690×; ⚠ transcription drop; unreliable plate only); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (AN3 CA 0.131×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.790× | -3.2 | 0.50 | 30/48 (H4, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.732× | -3.0 | 0.50 | 24/48 (AsPC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10014. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 39.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.287× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 21.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.53× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[PANC-1 (line)]] | alt | 28.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.51× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SW480 (line)]] | alt | 37.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A-172 (line)]] | wt | 36.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A549 (line)]] | wt | 30.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.17× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[AN3 CA (line)]] | alt | 42.3 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.131× (z -8.6) |
| [[HOP62 (line)]] | alt | 36.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 21.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.36× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H1573 (line)]] | alt | 18.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H1792 (line)]] | alt | 33.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 32.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SNU-423 (line)]] | alt | 28.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.70× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SW 1271 (line)]] | alt | 53.0 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0690× (z -9.3) ⚠ transcription drop; unreliable plate only |
| [[A498 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10014), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPA3]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 | STRING 514 |
| [[MTBP]] | +0.62 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[TPRKB]] | +0.61 | +0.61 / +0.63 | both halves | 7e-06 | STRING 472 |
| [[MRPL13]] | +0.60 | +0.63 / +0.59 | both halves | 7e-06 | STRING 428 |
| [[RPA2]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[DSN1]] | +0.58 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[CENPQ]] | +0.57 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[CWF19L1]] | +0.55 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[CENPW]] | +0.54 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[MMUT]] | +0.53 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[SIVA1]] | +0.53 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[SNRPC]] | +0.53 | +0.58 / +0.51 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 863 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KTN1-AS1]] | -0.48 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[PRRC2B]] | -0.47 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[CDV3]] | -0.46 | -0.43 / -0.37 | both halves | 7e-05 |  |
| [[TULP4]] | -0.46 | -0.48 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.427). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-27.9, -48.2); signed map (-37.5, -31.4). **Vector** length 57.4, 14.0% of its response variance represented; |z| ≥ 3 in 557 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.3 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | -0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +0.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.0 | -2.2 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | +0.9 | +1.4 |
|  | [[GSK1059615 (drug)]] 0.05 µM |  | +0.8 | +1.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -1.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.2 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | +0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | +0.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.3 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | LSM3 homolog, U6 small nuclear RNA and mRNA degradation associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:14,178,817-14,201,122 (+) |
| Ensembl biotype | protein_coding |
| Also known as | YLR438C, SMX4, USS2 |
| Gene groups (HGNC) | LSm proteins |
| Reactome | 6 pathways, smallest: mRNA decay by 5' to 3' exoribonuclease; Deadenylation-dependent mRNA decay; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P62310](https://www.uniprot.org/uniprotkb/P62310) (U6 snRNA-associated Sm-like protein LSm3):

> Plays a role in pre-mRNA splicing as component of the U4/U6-U5 tri-snRNP complex that is involved in spliceosome assembly, and as component of the precatalytic spliceosome (spliceosome B complex). The heptameric LSM2-8 complex binds specifically to the 3'-terminal U-tract of U6 snRNA.

**Summary**, from NCBI Gene [27258](https://www.ncbi.nlm.nih.gov/gene/27258):

> Sm-like proteins were identified in a variety of organisms based on sequence homology with the Sm protein family (see SNRPD2; MIM 601061). Sm-like proteins contain the Sm sequence motif, which consists of 2 regions separated by a linker of variable length that folds as a loop. The Sm-like proteins are thought to form a stable heteromer present in tri-snRNP particles, which are important for pre-mRNA splicing.[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:17874](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17874) · Entrez [27258](https://www.ncbi.nlm.nih.gov/gene/27258) · UniProt [P62310](https://www.uniprot.org/uniprotkb/P62310) · Ensembl [ENSG00000170860](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170860)

## Data

Gene col 10014: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10014); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10014, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10014]; `tensor/DDL_lfc|DDL_z.npy` [10014]; `embed/gene_vectors.npy` [10014]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10014 or target_col == 10014). Every well: [[LSM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LSM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
