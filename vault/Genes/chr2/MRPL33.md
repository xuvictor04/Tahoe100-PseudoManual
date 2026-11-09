---
symbol: "MRPL33"
type: "gene"
col: 14342
ensembl_id: "ENSG00000243147"
name: "mitochondrial ribosomal protein L33"
location: "2p23.2"
module: 48
arm: "+"
pooled_cpm: 51.53
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# MRPL33

*mitochondrial ribosomal protein L33* — 2p23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.83× (z +9.2, q 2e-17, up in 46 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +5.2, q 2e-05, up in 42 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (A549 6.41×, SHP-77 5.48×, SNU-423 5.51×, NCI-H1792 5.98×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (A549 5.12×, NCI-H1573 4.47×, NCI-H1792 5.28×, SK-MEL-2 5.21×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA1]] (+0.77, fdr 7e-06), [[COX17]] (+0.76, fdr 7e-06), [[UQCRB]] (+0.76, fdr 7e-06, ⚠ UQCRB in the vector space only through flagged drug-doses), [[ATP5F1E]] (+0.74, fdr 7e-06); moves opposite to [[PSMG1]] (-0.70, fdr 1e-05), [[FANCG]] (-0.68, fdr 9e-06), [[SIGMAR1]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14342.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (A549 6.41×, SHP-77 5.48×, SNU-423 5.51×, NCI-H1792 5.98×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (A549 5.12×, NCI-H1573 4.47×, NCI-H1792 5.28×, SK-MEL-2 5.21×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.83×** | +9.2 | 2e-17 | 46/47 (A549, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.99×** | +7.6 | 8e-12 | 42/42 (A549, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.57×** | +6.3 | 5e-08 | 42/43 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +5.3 | 1e-05 | 44/47 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +5.2 | 2e-05 | 42/48 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.99×** | +5.0 | 6e-05 | 37/48 (SW480, NCI-H1573, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +4.0 | 0.005 | 35/48 (NCI-H23, SW480, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14342.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Folic acid (drug)]] 5 µM |  | 0.709× | -3.4 | 0.19 | 37/48 (PANC-1, SW 1271, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.623× | -3.4 | 0.19 | 41/48 (HT-29, HEC-1-A, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14342. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 73.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.41× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1573 (line)]] | alt | 50.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.47× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1792 (line)]] | alt | 35.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.98× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HOP62 (line)]] | alt | 40.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LOX-IMVI (line)]] | wt | 35.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.09× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LS 180 (line)]] | wt | 58.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.41× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 37.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.39× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H460 (line)]] | wt | 47.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SHP-77 (line)]] | alt | 46.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 47.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.21× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SNU-423 (line)]] | alt | 45.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW480 (line)]] | alt | 55.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 65.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 95.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 75.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14342), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 15 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA1]] | +0.77 | +0.74 / +0.73 | both halves | 7e-06 | STRING 556 |
| [[COX17]] | +0.76 | +0.73 / +0.78 | both halves | 7e-06 | STRING 524 |
| [[UQCRB]] ⚠ | +0.76 | +0.68 / +0.80 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5F1E]] | +0.74 | +0.64 / +0.77 | both halves | 7e-06 | STRING 523 |
| [[RPS19]] | +0.70 | +0.57 / +0.76 | both halves | 1e-05 |  |
| [[GABARAPL2]] | +0.70 | +0.63 / +0.78 | both halves | 7e-06 |  |
| [[COX7A2]] ⚠ | +0.69 | +0.67 / +0.68 | both halves | 7e-06 | STRING 535; ⚠ in the vector space only through flagged drug-doses |
| [[RPL37A]] ⚠ | +0.68 | +0.58 / +0.76 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[COX6B1]] | +0.68 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[SERF2]] | +0.68 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[RPS29]] | +0.68 | +0.59 / +0.74 | both halves | 7e-06 | STRING 964 |
| [[ATP5ME]] | +0.67 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[ATP5MK]] | +0.66 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[RPL36]] | +0.66 | +0.58 / +0.76 | both halves | 7e-06 |  |
| [[HOTAIRM1]] | +0.66 | +0.59 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMG1]] | -0.70 | -0.49 / -0.70 | both halves | 1e-05 | STRING 822 |
| [[FANCG]] | -0.68 | -0.57 / -0.69 | both halves | 9e-06 |  |
| [[SIGMAR1]] | -0.65 | -0.59 / -0.69 | both halves | 7e-06 |  |
| [[HGH1]] | -0.64 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[GPS1]] | -0.64 | -0.64 / -0.57 | both halves | 1e-05 |  |
| [[MTHFD1]] | -0.63 | -0.55 / -0.69 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.63 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[AP2M1]] | -0.62 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[AKAP11]] | -0.62 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[APEH]] | -0.61 | -0.63 / -0.57 | both halves | 9e-06 |  |
| [[HASPIN]] | -0.61 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[TWF1]] | -0.61 | -0.57 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.649). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-45.4, -23.8); signed map (-35.9, 8.8). **Vector** length 64.1, 21.7% of its response variance represented; |z| ≥ 3 in 550 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.55 to 31); *Respiratory electron transport* (reactome, mean cos +0.54 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.55 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +2.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +2.4 | +5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +1.7 | -0.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +0.1 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -4.1 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -3.5 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -3.4 | +6.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -3.0 | +3.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.7 | +1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | +0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | +0.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.5 | +0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -1.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.2 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L33 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.2 — chr2:27,771,717-27,988,087 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPL33L, bL33m; previously C2orf1 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [O75394](https://www.uniprot.org/uniprotkb/O75394) carries no function annotation.

**Summary**, from NCBI Gene [9553](https://www.ncbi.nlm.nih.gov/gene/9553):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14487](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14487) · Entrez [9553](https://www.ncbi.nlm.nih.gov/gene/9553) · UniProt [O75394](https://www.uniprot.org/uniprotkb/O75394) · Ensembl [ENSG00000243147](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243147)

## Data

Gene col 14342: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14342); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14342, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14342]; `tensor/DDL_lfc|DDL_z.npy` [14342]; `embed/gene_vectors.npy` [14342]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14342 or target_col == 14342). Every well: [[MRPL33 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL33.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
