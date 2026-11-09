---
symbol: "ATP5F1E"
type: "gene"
col: 4491
ensembl_id: "ENSG00000124172"
name: "ATP synthase F1 subunit epsilon"
location: "20q13.32"
module: 48
arm: "+"
pooled_cpm: 121.06
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# ATP5F1E

*ATP synthase F1 subunit epsilon* — 20q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.84× (z +8.6, q 4e-15, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.78× (z +4.5, q 8e-04, up in 39 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (LoVo 7.09×, LS 180 6.23×, NCI-H1792 11.3×, KATO III 7.50×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (HOP62 6.79×, HCT15 8.05×, NCI-H23 5.85×, MIA PaCa-2 7.33×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UQCRB]] (+0.86, fdr 7e-06, ⚠ UQCRB in the vector space only through flagged drug-doses), [[COX4I1]] (+0.83, fdr 7e-06, ⚠ COX4I1 in the vector space only through flagged drug-doses), [[ROMO1]] (+0.81, fdr 7e-06), [[NDUFA1]] (+0.80, fdr 7e-06), [[UBL5]] (+0.80, fdr 7e-06); moves opposite to [[PSMG1]] (-0.73, fdr 9e-06), [[ZNF460]] (-0.69, fdr 1e-05), [[PNPO]] (-0.65, fdr 2e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4491.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (LoVo 7.09×, LS 180 6.23×, NCI-H1792 11.3×, KATO III 7.50×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (HOP62 6.79×, HCT15 8.05×, NCI-H23 5.85×, MIA PaCa-2 7.33×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **5.84×** | +8.6 | 4e-15 | 49/49 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **4.54×** | +8.0 | 5e-13 | 44/44 (HOP62, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.24×** | +5.9 | 5e-07 | 45/45 (LS 180, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.83×** | +5.7 | 2e-06 | 48/48 (SW480, COLO 205, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.41×** | +4.6 | 4e-04 | 47/47 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +4.5 | 8e-04 | 39/49 (A-172, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **2.17×** | +4.2 | 0.002 | 46/48 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4491.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Folic acid (drug)]] 5 µM |  | 0.666× | -3.2 | 0.58 | 43/48 (NCI-H2347, SW 1088, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.342× | -3.1 | 0.58 | 45/49 (BT-474, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, +0.75 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4491. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 88.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.03× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[C32 (line)]] | wt | 87.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.90× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HCT15 (line)]] | alt | 64.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.05× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HOP62 (line)]] | alt | 92.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.79× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 62.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.65× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SW480 (line)]] | alt | 118 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.67× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[COLO 205 (line)]] | alt | 72.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.61× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HEC-1-A (line)]] | alt | 69.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[KATO III (line)]] | alt | 145 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.50× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[LoVo (line)]] | wt | 92.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.09× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[LOX-IMVI (line)]] | wt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.96× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[LS 180 (line)]] | wt | 48.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.23× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1573 (line)]] | alt | 109 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.49× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1792 (line)]] | alt | 92.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.3× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H23 (line)]] | alt | 169 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.85× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[Panc 03.27 (line)]] | alt | 112 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.78× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[PANC-1 (line)]] | alt | 112 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-172 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 160 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 96.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 156 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 89.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 75.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 147 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 156 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 107 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 90.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 160 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 98.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 96.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 91.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 102 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4491), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 21 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCRB]] ⚠ | +0.86 | +0.78 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 709; ⚠ in the vector space only through flagged drug-doses |
| [[COX4I1]] ⚠ | +0.83 | +0.78 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 700; ⚠ in the vector space only through flagged drug-doses |
| [[ROMO1]] | +0.81 | +0.81 / +0.81 | both halves | 7e-06 |  |
| [[UQCRQ]] ⚠ | +0.81 | +0.77 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 863; ⚠ in the vector space only through flagged drug-doses |
| [[NDUFA1]] | +0.80 | +0.76 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 840 |
| [[UBL5]] | +0.80 | +0.75 / +0.82 | both halves | 7e-06 |  |
| [[COX6B1]] | +0.80 | +0.76 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 658 |
| [[RPS29]] | +0.80 | +0.72 / +0.82 | both halves | 7e-06 | STRING 467 |
| [[RPLP2]] | +0.79 | +0.73 / +0.82 | both halves | 7e-06 |  |
| [[RPLP1]] | +0.79 | +0.68 / +0.82 | both halves | 7e-06 |  |
| [[RPS19]] | +0.79 | +0.70 / +0.82 | both halves | 7e-06 | STRING 506 |
| [[COX6A1]] | +0.79 | +0.73 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 722 |
| [[COX6C]] | +0.79 | +0.67 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 796 |
| [[COX7C]] | +0.78 | +0.70 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 915 |
| [[RPS12]] | +0.78 | +0.66 / +0.83 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMG1]] | -0.73 | -0.57 / -0.76 | both halves | 9e-06 |  |
| [[ZNF460]] | -0.69 | -0.52 / -0.73 | both halves | 1e-05 |  |
| [[PNPO]] | -0.65 | -0.47 / -0.68 | both halves | 2e-05 |  |
| [[PRMT5]] | -0.61 | -0.58 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.807). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-46.1, -23.1); signed map (-34.9, 9.8). **Vector** length 67.1, 39.8% of its response variance represented; |z| ≥ 3 in 559 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Respiratory electron transport* (reactome, mean cos +0.64 to 24); *Complex IV assembly* (reactome, mean cos +0.69 to 11); *Cytoprotection by HMOX1* (reactome, mean cos +0.70 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +1.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +3.3 | +5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.6 | +0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | -1.2 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +1.4 | -0.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | -0.4 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -4.5 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -4.5 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -4.4 | +8.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.6 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | +1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.0 | +1.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | +0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ATP synthase F1 subunit epsilon |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.32 — chr20:59,025,475-59,032,345 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ATP5E |
| Gene groups (HGNC) | Mitochondrial complex V: ATP synthase subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 5 pathways, smallest: Formation of ATP by chemiosmotic coupling; Cristae formation; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P56381](https://www.uniprot.org/uniprotkb/P56381) (ATP synthase F(1) complex subunit epsilon, mitochondrial):

> Subunit epsilon, of the mitochondrial membrane ATP synthase complex (F(1)F(0) ATP synthase or Complex V) that produces ATP from ADP in the presence of a proton gradient across the membrane which is generated by electron transport complexes of the respiratory chain. ATP synthase complex consist of a soluble F(1) head domain - the catalytic core - and a membrane F(1) domain - the membrane proton channel. These two domains are linked by a central stalk rotating inside the F(1) region and a …

**Summary**, from NCBI Gene [514](https://www.ncbi.nlm.nih.gov/gene/514):

> This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic portion of mitochondrial ATP synthase consists of 5 different subunits (alpha, beta, gamma, …

**Accessions** — [HGNC:838](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:838) · Entrez [514](https://www.ncbi.nlm.nih.gov/gene/514) · UniProt [P56381](https://www.uniprot.org/uniprotkb/P56381) · Ensembl [ENSG00000124172](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124172)

## Data

Gene col 4491: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4491); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4491, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4491]; `tensor/DDL_lfc|DDL_z.npy` [4491]; `embed/gene_vectors.npy` [4491]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4491 or target_col == 4491). Every well: [[ATP5F1E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP5F1E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
