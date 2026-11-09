---
symbol: "SNRPF"
type: "gene"
col: 6294
ensembl_id: "ENSG00000139343"
name: "small nuclear ribonucleoprotein polypeptide F"
location: "12q23.1"
module: 4
arm: "+"
pooled_cpm: 48.62
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# SNRPF

*small nuclear ribonucleoprotein polypeptide F* — 12q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.21× (z +9.2, q 3e-17, up in 44 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.66× (z +4.0, q 0.005, up in 40 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (NCI-H1792 7.82×, A549 5.94×, NCI-H460 4.95×, PANC-1 4.52×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1792 6.15×, H4 7.63×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 4.18×; ⚠ cell-cycle shift, explains ~70% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[AZD2858 (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0714×; ⚠ toxic).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNRPD1]] (+0.66, fdr 7e-06), [[NDUFC2]] (+0.63, fdr 1e-05), [[MRPS9]] (+0.60, fdr 1e-05); moves opposite to [[YPEL5]] (-0.54, fdr 1e-05), [[TLN1]] (-0.54, fdr 7e-05), [[CORO1B]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6294.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (NCI-H1792 7.82×, A549 5.94×, NCI-H460 4.95×, PANC-1 4.52×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1792 6.15×, H4 7.63×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 4.18×; ⚠ cell-cycle shift, explains ~70% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **3.21×** | +9.2 | 3e-17 | 44/45 (NCI-H1792, A549, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.38×** | +6.8 | 3e-09 | 45/47 (SW480, NCI-H1573, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **2.53×** | +6.7 | 3e-09 | 37/42 (NCI-H1792, H4, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.33×** | +6.1 | 1e-07 | 41/45 (KATO III, A549, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.18×** | +5.7 | 2e-06 | 45/47 (NCI-H1573, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.98×** | +5.4 | 8e-06 | 42/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~69% of this change | **1.71×** | +4.2 | 0.002 | 37/46 (HT-29, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +4.0 | 0.005 | 40/48 (HS-578T, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.62×** | +3.8 | 0.009 | 31/48 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.62×** | +3.8 | 0.009 | 38/48 (HOP62, C32, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~64% of this change | **1.65×** | +3.6 | 0.014 | 30/47 (A-172, NCI-H1792, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.64×** | +3.6 | 0.016 | 33/48 (NCI-H1573, SNU-423, …) | rises with dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.11×** | +3.1 | 0.096 | 21/34 (HS-578T, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.47× | +3.0 | 0.10 | 32/48 (HT-29, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6294.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[AZD2858 (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0714×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bimiralisib (drug)]] 5 µM |  | 0.438× | -3.4 | 0.40 | 35/48 (A498, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.615× | -3.2 | 0.44 | 31/48 (KATO III, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.63 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6294. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 42.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.97× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 35.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | [[AZD2858 (drug)]] 0.5 µM 0.0714× (z -8.6) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 43.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.82× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[A498 (line)]] | wt | 37.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[A549 (line)]] | wt | 52.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.94× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[Hs 766T (line)]] | wt | 27.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[HT-29 (line)]] | alt | 34.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.38× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[NCI-H1573 (line)]] | alt | 36.1 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.18× (z +8.5) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[NCI-H460 (line)]] | wt | 67.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[PANC-1 (line)]] | alt | 48.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[SW480 (line)]] | alt | 60.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[A-172 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 57.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 72.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 56.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 75.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6294), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPD1]] | +0.66 | +0.63 / +0.67 | both halves | 7e-06 | same gene group; pathway: ATP-dependent chromatin remodelers; STRING 999 |
| [[NDUFC2]] | +0.63 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[MRPS9]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[TANGO6]] | +0.56 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[ATP5MF]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[SNRPE]] | +0.56 | +0.50 / +0.59 | both halves | 1e-05 | same gene group; pathway: ATP-dependent chromatin remodelers; STRING 999 |
| [[TOMM5]] | +0.54 | +0.30 / +0.68 | both halves | 2e-04 |  |
| [[CDIN1]] | +0.54 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[DNPH1]] | +0.54 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[IMMP1L]] | +0.52 | +0.28 / +0.62 | both halves | 3e-04 |  |
| [[ERCC8]] | +0.52 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[ABCB7]] | +0.52 | +0.46 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YPEL5]] | -0.54 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[TLN1]] | -0.54 | -0.38 / -0.59 | both halves | 7e-05 |  |
| [[CORO1B]] | -0.54 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[MAF1]] | -0.53 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[TCP11L2]] | -0.51 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[HECA]] | -0.50 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[HIPK1]] | -0.49 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[STYX]] | -0.48 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[EBLN3P]] | -0.47 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[EMD]] | -0.47 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[CYLD]] | -0.47 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[ATG9A]] | -0.46 | -0.42 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.326). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-51.4, -17.7); signed map (-38.8, -25.4). **Vector** length 52.5, 15.2% of its response variance represented; |z| ≥ 3 in 691 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +1.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.9 | +2.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +1.8 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.8 | +5.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +0.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +0.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +0.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~69% of this change | -1.9 | +4.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +2.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~64% of this change | -1.6 | +3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | +0.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.2 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.1 | +2.9 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear ribonucleoprotein polypeptide F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.1 — chr12:95,858,952-95,903,828 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Sm-F |
| Gene groups (HGNC) | Sm spliceosomal proteins |
| Reactome | 24 pathways, smallest: SLBP independent Processing of Histone Pre-mRNAs; SLBP Dependent Processing of Replication-Dependent Histone Pre-mRNAs; Processing of Capped Intronless Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P62306](https://www.uniprot.org/uniprotkb/P62306) (Small nuclear ribonucleoprotein F):

> Plays a role in pre-mRNA splicing as a core component of the spliceosomal U1, U2, U4 and U5 small nuclear ribonucleoproteins (snRNPs), the building blocks of the spliceosome. Component of both the pre-catalytic spliceosome B complex and activated spliceosome C complexes. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs. As part of the U7 snRNP it is involved in histone 3'-end processing.

**Summary**, from NCBI Gene [6636](https://www.ncbi.nlm.nih.gov/gene/6636):

> Enables RNA binding activity. Involved in spliceosomal snRNP assembly. Located in cytosol and nucleus. Part of several cellular components, including methylosome; nucleus; and pICln-Sm protein complex. Biomarker of nasopharynx carcinoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11162](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11162) · Entrez [6636](https://www.ncbi.nlm.nih.gov/gene/6636) · UniProt [P62306](https://www.uniprot.org/uniprotkb/P62306) · Ensembl [ENSG00000139343](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139343)

## Data

Gene col 6294: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6294); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6294, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6294]; `tensor/DDL_lfc|DDL_z.npy` [6294]; `embed/gene_vectors.npy` [6294]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6294 or target_col == 6294). Every well: [[SNRPF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNRPF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
