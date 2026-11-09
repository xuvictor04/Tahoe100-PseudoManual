---
symbol: "ATP5PD"
type: "gene"
col: 9552
ensembl_id: "ENSG00000167863"
name: "ATP synthase peripheral stalk subunit d"
location: "17q25.1"
module: 48
arm: "+"
pooled_cpm: 48.75
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# ATP5PD

*ATP synthase peripheral stalk subunit d* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.02× (z +9.7, q 1e-19, up in 46 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.47× (z +3.8, q 0.014, up in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (NCI-H1792 8.42×, PANC-1 5.66×, HEC-1-A 5.20×, C32 6.53×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H460 5.48×, SW480 5.06×, PANC-1 4.60×, LoVo 5.33×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.124×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP5MK]] (+0.85, fdr 7e-06), [[ROMO1]] (+0.85, fdr 7e-06), [[COX6B1]] (+0.84, fdr 7e-06).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9552.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (NCI-H1792 8.42×, PANC-1 5.66×, HEC-1-A 5.20×, C32 6.53×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H460 5.48×, SW480 5.06×, PANC-1 4.60×, LoVo 5.33×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **4.02×** | +9.7 | 1e-19 | 46/47 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.48×** | +8.4 | 1e-14 | 39/40 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.42×** | +5.7 | 2e-06 | 37/43 (C32, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +4.9 | 1e-04 | 44/47 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.81×** | +4.1 | 0.004 | 38/46 (CFPAC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.014 | 30/48 (NCI-H2347, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Sulfatinib (drug)]] 5 µM |  | 1.57× | +3.1 | 0.18 | 32/48 (Hs 766T, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9552.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.124×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | 0.392× | -3.4 | 0.36 | 30/48 (A-427, NCI-H23, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | 0.424× | -3.1 | 0.44 | 35/48 (NCI-H23, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.733× | -3.0 | 0.44 | 29/48 (Panc 03.27, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9552. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 45.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A498 (line)]] | wt | 53.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[C32 (line)]] | wt | 30.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.53× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HEC-1-A (line)]] | alt | 70.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.20× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HOP62 (line)]] | alt | 45.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.59× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LoVo (line)]] | wt | 38.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.33× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H1573 (line)]] | alt | 34.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.14× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H460 (line)]] | wt | 46.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.48× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[PANC-1 (line)]] | alt | 61.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW480 (line)]] | alt | 49.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.06× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A549 (line)]] | wt | 55.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[C-33 A (line)]] | alt | 36.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.92× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[CHP-212 (line)]] | wt | 64.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.124× (z -9.1) |
| [[HS-578T (line)]] | alt | 44.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.59× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[LOX-IMVI (line)]] | wt | 47.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 44.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.14× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1792 (line)]] | alt | 38.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.42× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SNU-1 (line)]] | wt | 32.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.58× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SNU-423 (line)]] | alt | 68.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW 900 (line)]] | alt | 37.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.46× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-427 (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9552), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5MK]] | +0.85 | +0.65 / +0.90 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999 |
| [[ROMO1]] | +0.85 | +0.73 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[COX6B1]] | +0.84 | +0.62 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 879 |
| [[UQCRB]] ⚠ | +0.84 | +0.71 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 976; ⚠ in the vector space only through flagged drug-doses |
| [[UQCRQ]] ⚠ | +0.83 | +0.66 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 967; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MJ]] | +0.82 | +0.64 / +0.87 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 998 |
| [[NDUFA1]] | +0.81 | +0.64 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 725 |
| [[ATP5ME]] | +0.81 | +0.62 / +0.86 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[COX7C]] | +0.80 | +0.59 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 962 |
| [[TOMM7]] | +0.79 | +0.62 / +0.80 | both halves | 7e-06 | STRING 469 |
| [[COMMD6]] | +0.79 | +0.52 / +0.84 | both halves | 1e-05 |  |
| [[COX4I1]] ⚠ | +0.78 | +0.62 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 952; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5F1E]] | +0.77 | +0.66 / +0.79 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[COX6A1]] | +0.77 | +0.54 / +0.85 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 895 |
| [[COX6C]] | +0.77 | +0.52 / +0.84 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 975 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.866). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-45.9, -22.4); signed map (-34.8, 9.0). **Vector** length 48.1, 14.7% of its response variance represented; |z| ≥ 3 in 463 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Respiratory electron transport* (reactome, mean cos +0.68 to 24); *Complex IV assembly* (reactome, mean cos +0.71 to 11); *Cytoprotection by HMOX1* (reactome, mean cos +0.72 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.7 | +2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.4 | -0.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.3 | +0.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.3 | +1.7 |
|  | [[Ciclopirox (drug)]] 5 µM |  | +0.9 | -0.8 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | +0.8 | +0.9 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +0.8 | +0.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.8 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -3.6 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -3.6 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -3.1 | +9.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | -2.2 | +4.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.4 | -0.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.3 | +1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ATP synthase peripheral stalk subunit d |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,038,863-75,046,985 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATPQ, ATP5JD; previously ATP5H |
| Gene groups (HGNC) | Mitochondrial complex V: ATP synthase subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 6 pathways, smallest: Formation of ATP by chemiosmotic coupling; Cristae formation; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [O75947](https://www.uniprot.org/uniprotkb/O75947) (ATP synthase peripheral stalk subunit d, mitochondrial):

> Subunit d, of the mitochondrial membrane ATP synthase complex (F(1)F(0) ATP synthase or Complex V) that produces ATP from ADP in the presence of a proton gradient across the membrane which is generated by electron transport complexes of the respiratory chain. ATP synthase complex consist of a soluble F(1) head domain - the catalytic core - and a membrane F(1) domain - the membrane proton channel. These two domains are linked by a central stalk rotating inside the F(1) region and a stationary …

**Summary**, from NCBI Gene [10476](https://www.ncbi.nlm.nih.gov/gene/10476):

> Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. It is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, which comprises the proton channel. The F1 complex consists of 5 different subunits (alpha, beta, gamma, delta, and epsilon) assembled in a ratio of 3 alpha, 3 beta, and a single representative of the other 3. …

**Accessions** — [HGNC:845](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:845) · Entrez [10476](https://www.ncbi.nlm.nih.gov/gene/10476) · UniProt [O75947](https://www.uniprot.org/uniprotkb/O75947) · Ensembl [ENSG00000167863](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167863)

## Data

Gene col 9552: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9552); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9552, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9552]; `tensor/DDL_lfc|DDL_z.npy` [9552]; `embed/gene_vectors.npy` [9552]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9552 or target_col == 9552). Every well: [[ATP5PD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP5PD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
