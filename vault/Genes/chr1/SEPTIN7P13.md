---
symbol: "SEPTIN7P13"
type: "gene"
col: 11687
ensembl_id: "ENSG00000185495"
name: "septin 7 pseudogene 13"
location: "1q42.11"
module: 42
arm: "+"
pooled_cpm: 5.58
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# SEPTIN7P13

*septin 7 pseudogene 13* — 1q42.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.60× (z +4.6, q 0.003, up in 16 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Lidocaine (hydrochloride) (drug)]] 0.5 µM: 1.47× (z +3.7, q 0.035, up in 11 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.615× (z -6.7, q 1e-08, down in 23 of 39 measured lines) ⚠ cell-cycle shift, explains ~86% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.595× (z -5.1, q 7e-05, down in 20 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 0.291×, A-172 0.220×, PANC-1 0.291×; ⚠ cell-cycle shift, explains ~86% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (A498 0.159×, PANC-1 0.158×; ⚠ cell-cycle shift, explains ~58% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.0441×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Cobimetinib (drug)]] 0.05 µM in 1 line (A-172 0.0841×); [[Harringtonine (drug)]] 0.5 µM in 1 line (A498 0.188×); [[ULK-101 (drug)]] 0.05 µM in 1 line (A-427 0.0699×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01409]] (+0.77, fdr 7e-06), [[SEPTIN7P14]] (+0.67, fdr 1e-05), [[PMS2P3-1]] (+0.64, fdr 7e-06); moves opposite to [[BPTF]] (-0.60, fdr 1e-05), [[HES1]] (-0.56, fdr 2e-05), [[LRRC37A2]] (-0.55, fdr 2e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11687.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.60×** | +4.6 | 0.003 | 16/45 (A-427, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +3.9 | 0.033 | 6/18 (NCI-H1573, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +3.7 | 0.035 | 11/40 (PANC-1, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.043 | 10/44 (MIA PaCa-2, HT-29, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.38× | +3.2 | 0.17 | 4/45 (LoVo, SW1417, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | 1.39× | +3.1 | 0.17 | 4/32 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.37× | +3.1 | 0.17 | 9/42 (SW 900, A-172, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | 1.36× | +3.0 | 0.18 | 9/46 (SNU-423, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11687.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 0.291×, A-172 0.220×, PANC-1 0.291×; ⚠ cell-cycle shift, explains ~86% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (A498 0.159×, PANC-1 0.158×; ⚠ cell-cycle shift, explains ~58% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.0441×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Cobimetinib (drug)]] 0.05 µM in 1 line (A-172 0.0841×); [[Harringtonine (drug)]] 0.5 µM in 1 line (A498 0.188×); [[ULK-101 (drug)]] 0.05 µM in 1 line (A-427 0.0699×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.615×** | -6.7 | 1e-08 | 23/39 (A498, A-172, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.564×** | -5.4 | 2e-05 | 22/43 (A498, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.595×** | -5.1 | 7e-05 | 20/44 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.621×** | -4.7 | 5e-04 | 17/38 (A498, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.622×** | -4.5 | 9e-04 | 15/30 (NCI-H460, LoVo, …) | top dose only | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.637× | -3.0 | 0.24 | 10/40 (HT-29, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11687. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 11.9 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0441× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.188× (z -9.4) |
| [[A-172 (line)]] | wt | 6.88 | 0 | 2 (1 ⚠) | — | [[Cobimetinib (drug)]] 0.05 µM 0.0841× (z -9.8) |
| [[PANC-1 (line)]] | alt | 5.38 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.158× (z -8.8) ⚠ cell-cycle shift, explains ~58% of this change |
| [[A-427 (line)]] | wt | 4.66 | 0 | 1 | — | [[ULK-101 (drug)]] 0.05 µM 0.0699× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 7.82 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.169× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change |
| [[A549 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11687), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01409]] | +0.77 | +0.75 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[SEPTIN7P14]] | +0.67 | +0.54 / +0.75 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | +0.64 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[CRYBB2P1]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[CCNY-AS1]] | +0.61 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[NAPB]] | +0.59 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[LINC03009]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[TMEM248]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[TIMM10B]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[PMS2P3]] | +0.57 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[STRAP]] | +0.56 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[NOMO2]] | +0.56 | +0.59 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BPTF]] | -0.60 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[HES1]] | -0.56 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[LRRC37A2]] | -0.55 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[RSF1]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[EIF4EBP3]] | -0.55 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[NFAT5]] | -0.54 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[SFR1]] | -0.54 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[THG1L]] | -0.53 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[ANKRD26]] | -0.53 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[OFD1]] | -0.53 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[KMT2A]] | -0.53 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[ZNF518A]] | -0.52 | -0.59 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.501). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.1, -28.2); signed map (-54.9, 2.2). **Vector** length 55.8, 7.46% of its response variance represented; |z| ≥ 3 in 948 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.2 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.5 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | +1.4 | +3.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.4 | +1.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.0 | +1.7 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | +1.0 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.0 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | -4.9 | -6.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -4.6 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.1 | -4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.0 | -5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.9 | -0.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[Thymol (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.3 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | septin 7 pseudogene 13 |
| Locus type | pseudogene |
| Location | 1q42.11 — chr1:223,995,895-224,003,654 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55092](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55092) · Entrez [100287497](https://www.ncbi.nlm.nih.gov/gene/100287497) · Ensembl [ENSG00000185495](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185495)

## Data

Gene col 11687: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11687); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11687, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11687]; `tensor/DDL_lfc|DDL_z.npy` [11687]; `embed/gene_vectors.npy` [11687]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11687 or target_col == 11687). Every well: [[SEPTIN7P13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEPTIN7P13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
