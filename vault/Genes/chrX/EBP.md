---
symbol: "EBP"
type: "gene"
col: 7156
ensembl_id: "ENSG00000147155"
name: "EBP cholestenol delta-isomerase"
location: "Xp11.23"
module: 86
arm: "+"
pooled_cpm: 20.15
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# EBP

*EBP cholestenol delta-isomerase* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.30× (z +10.0, q 1e-20, up in 35 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Berbamine (drug)]] 5 µM: 1.85× (z +7.4, q 5e-11, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.724× (z -3.9, q 0.057, down in 28 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (KATO III 0.233×, RKO 0.231×); [[Dinaciclib (drug)]] 5 µM in 1 line (BT-474 0.0677×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SREBF2]] (+0.78, fdr 7e-06), [[FDPS]] (+0.77, fdr 7e-06), [[IDI1]] (+0.76, fdr 7e-06); moves opposite to [[MTHFSD]] (-0.43, fdr 1e-04), [[ZXDA]] (-0.42, fdr 1e-04), [[DUS4L]] (-0.41, fdr 9e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7156.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **3.30×** | +10.0 | 1e-20 | 35/37 (A-172, J82, …) | all doses, stronger at high dose | composition shift |
| [[Berbamine (drug)]] 5 µM |  | **1.85×** | +7.4 | 5e-11 | 41/47 (HT-29, LoVo, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.78×** | +6.9 | 1e-09 | 36/47 (A549, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **2.29×** | +6.8 | 2e-09 | 20/27 (A-172, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.01×** | +5.5 | 5e-06 | 19/30 (J82, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +4.8 | 1e-04 | 25/39 (J82, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.72×** | +4.6 | 3e-04 | 31/47 (SNU-423, HT-29, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.72×** | +4.4 | 7e-04 | 30/47 (SNU-423, A-172, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.68×** | +4.4 | 8e-04 | 26/41 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.61×** | +4.0 | 0.004 | 24/47 (NCI-H460, MIA PaCa-2, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.59×** | +3.9 | 0.005 | 25/45 (LoVo, J82, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **1.57×** | +3.7 | 0.011 | 21/38 (LoVo, C32, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.53×** | +3.6 | 0.015 | 22/47 (A498, C32, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.53×** | +3.5 | 0.023 | 24/47 (NCI-H460, A498, …) | top dose only | plate-row cell shift |
| [[vincristine (drug)]] 5 µM |  | **2.02×** | +3.1 | 0.065 | 16/39 (SW1417, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ritonavir (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.065 | 16/47 (LS 180, PANC-1, …) | top dose only |  |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.071 | 14/47 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift |
| [[Arbutin (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.072 | 15/46 (SW480, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7156.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (KATO III 0.233×, RKO 0.231×); [[Dinaciclib (drug)]] 5 µM in 1 line (BT-474 0.0677×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.724×** | -3.9 | 0.057 | 28/45 (KATO III, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[BAY1125976 (drug)]] 5 µM |  | 0.481× | -3.2 | 0.24 | 17/47 (KATO III, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.492× | -3.2 | 0.24 | 16/47 (HCT15, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.691× | -3.1 | 0.24 | 18/45 (KATO III, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.508× | -3.0 | 0.29 | 18/43 (A-427, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7156. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 20.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.75× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A498 (line)]] | wt | 16.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[BT-474 (line)]] | alt | 33.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0677× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[HT-29 (line)]] | alt | 23.9 | 1 | 0 | [[Berbamine (drug)]] 5 µM 3.55× (z +9.3) | — |
| [[J82 (line)]] | alt | 30.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[KATO III (line)]] | alt | 59.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -11.6) |
| [[LoVo (line)]] | wt | 17.5 | 1 | 0 | [[Berbamine (drug)]] 5 µM 3.21× (z +9.0) | — |
| [[RKO (line)]] | wt | 16.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -8.8) |
| [[SNU-423 (line)]] | alt | 16.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.74× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A-427 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.21 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 36.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7156), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SREBF2]] | +0.78 | +0.72 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[FDPS]] | +0.77 | +0.80 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 675 |
| [[IDI1]] | +0.76 | +0.79 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 622 |
| [[HMGCR]] | +0.76 | +0.75 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 655 |
| [[SQLE]] | +0.76 | +0.77 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 697 |
| [[MVD]] | +0.74 | +0.75 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 668 |
| [[FDFT1]] | +0.73 | +0.71 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 783 |
| [[ACAT2]] | +0.72 | +0.70 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 701 |
| [[DHCR7]] | +0.71 | +0.76 / +0.57 | both halves | 8e-06 | same gene group; pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 966 |
| [[MSMO1]] | +0.70 | +0.69 / +0.60 | both halves | 7e-06 | pathway: Cholesterol biosynthesis; STRING 740 |
| [[ERG28]] | +0.69 | +0.71 / +0.59 | both halves | 7e-06 | STRING 580 |
| [[ACSS2]] | +0.69 | +0.70 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTHFSD]] | -0.43 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[ZXDA]] | -0.42 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[DUS4L]] | -0.41 | -0.37 / -0.38 | both halves | 9e-05 |  |
| [[USP40]] | -0.41 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[C8orf33]] | -0.41 | -0.40 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[MTIF2]] | -0.41 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[POLR2M]] | -0.40 | -0.24 / -0.42 | both halves | 5e-04 |  |
| [[KRR1]] | -0.40 | -0.30 / -0.35 | both halves | 2e-04 |  |
| [[CCDC25]] | -0.40 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[GIN1]] | -0.39 | -0.36 / -0.29 | both halves | 2e-04 |  |
| [[SLC24A1]] | -0.39 | -0.36 / -0.30 | both halves | 2e-04 |  |
| [[SMARCE1]] | -0.39 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[TCTN1]] | -0.39 | -0.34 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.802). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.2, -48.9); signed map (-52.9, 32.5). **Vector** length 86.8, 23.2% of its response variance represented; |z| ≥ 3 in 772 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Regulation of cholesterol biosynthesis by SREBP (SREBF)* (reactome, mean cos +0.65 to 17); *Activation of gene expression by SREBF (SREBP)* (reactome, mean cos +0.65 to 16); *Lanosterol biosynthesis* (reactome, mean cos +0.71 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +5.4 | +6.9 |
|  | [[Berbamine (drug)]] 5 µM |  | +5.2 | +7.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | +3.3 | +3.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.2 | +4.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.7 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.9 | +4.4 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +3.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.2 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -1.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.7 | -3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | EBP cholestenol delta-isomerase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:48,521,799-48,528,716 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D8D7I, CPX, CPXD, CHO2; previously CDPX2 |
| Gene groups (HGNC) | AEBS complex subunits; EXPERA domain containing |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, APOPTOSIS, MTORC1_SIGNALING |
| Reactome | 5 pathways, smallest: Cholesterol biosynthesis from zymosterol (modified Kandutsch-Russell pathway); Cholesterol biosynthesis via desmosterol (Bloch pathway); Cholesterol biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15125](https://www.uniprot.org/uniprotkb/Q15125) (3-beta-hydroxysteroid-Delta(8),Delta(7)-isomerase):

> Isomerase that catalyzes the conversion of Delta(8)-sterols to their corresponding Delta(7)-isomers a catalytic step in the postlanosterol biosynthesis of cholesterol.; Component of the microsomal antiestrogen binding site (AEBS), a multiproteic complex at the ER membrane that consists of an association between EBP and 7-dehydrocholesterol reductase/DHCR7. This complex is responsible for cholesterol-5,6-epoxide hydrolase (ChEH) activity, which consists in the hydration of …

**Summary**, from NCBI Gene [10682](https://www.ncbi.nlm.nih.gov/gene/10682):

> The protein encoded by this gene is an integral membrane protein of the endoplasmic reticulum. It is a high affinity binding protein for the antiischemic phenylalkylamine Ca2+ antagonist [3H]emopamil and the photoaffinity label [3H]azidopamil. It is similar to sigma receptors and may be a member of a superfamily of high affinity drug-binding proteins in the endoplasmic reticulum of different tissues. This protein shares structural features with bacterial and eukaryontic drug transporting …

**Accessions** — [HGNC:3133](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3133) · Entrez [10682](https://www.ncbi.nlm.nih.gov/gene/10682) · UniProt [Q15125](https://www.uniprot.org/uniprotkb/Q15125) · Ensembl [ENSG00000147155](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147155)

## Data

Gene col 7156: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7156); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7156, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7156]; `tensor/DDL_lfc|DDL_z.npy` [7156]; `embed/gene_vectors.npy` [7156]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7156 or target_col == 7156). Every well: [[EBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
