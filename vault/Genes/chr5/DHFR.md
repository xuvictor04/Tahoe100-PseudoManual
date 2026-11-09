---
symbol: "DHFR"
type: "gene"
col: 13670
ensembl_id: "ENSG00000228716"
name: "dihydrofolate reductase"
location: "5q14.1"
module: 20
arm: "+"
pooled_cpm: 48.84
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# DHFR

*dihydrofolate reductase* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.46× (z +10.2, q 2e-21, up in 47 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.56× (z +3.6, q 0.032, up in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (HOP62 3.72×, HT-29 4.27×, A498 4.24×, NCI-H460 4.19×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (LoVo 4.02×, A-172 4.24×, HT-29 4.36×, MIA PaCa-2 5.10×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Bosentan (hydrate) (drug)]] 0.5 µM: 0.485× (z -6.0, q 1e-06, down in 46 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.145×; ⚠ cell-cycle shift, explains ~38% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (Panc 03.27 0.217×; ⚠ transcription drop; cell-cycle shift, explains ~29% of this change); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0575×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF4H]] (+0.78, fdr 7e-06), [[CTSZ]] (+0.77, fdr 7e-06), [[FKBP9]] (+0.76, fdr 7e-06); moves opposite to [[SMIM26]] (-0.77, fdr 1e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[MRPL36]] (-0.72, fdr 2e-04), [[ZNF593]] (-0.72, fdr 3e-05), [[PIGBOS1]] (-0.70, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13670.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (HOP62 3.72×, HT-29 4.27×, A498 4.24×, NCI-H460 4.19×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (LoVo 4.02×, A-172 4.24×, HT-29 4.36×, MIA PaCa-2 5.10×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.46×** | +10.2 | 2e-21 | 47/48 (HOP62, HT-29, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.37×** | +9.6 | 3e-19 | 42/42 (LoVo, A-172, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.33×** | +9.1 | 1e-17 | 42/44 (HOP62, LoVo, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.20× | +5.0 | 1e-04 | 16/49 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +3.6 | 0.032 | 30/48 (NCI-H460, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.23×** | +3.4 | 0.059 | 32/49 (C32, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13670.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.145×; ⚠ cell-cycle shift, explains ~38% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (Panc 03.27 0.217×; ⚠ transcription drop; cell-cycle shift, explains ~29% of this change); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0575×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.485×** | -6.0 | 1e-06 | 46/48 (HOP62, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | **0.567×** | -4.7 | 7e-04 | 44/48 (HOP62, NCI-H460, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **0.634×** | -3.8 | 0.029 | 30/47 (Panc 03.27, A549, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | 0.768× | -3.3 | 0.12 | 31/48 (HOP62, LS 180, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.683× | -3.2 | 0.16 | 23/47 (A-427, HCT15, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13670. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 43.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 50.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.24× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 42.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.24× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 50.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 43.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.02× (z +9.5) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 34.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.10× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 53.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -11.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H460 (line)]] | wt | 44.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +9.2) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 41.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.217× (z -9.5) ⚠ transcription drop; cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 54.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 43.7 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0575× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 48.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 70.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 64.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13670), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4H]] | +0.78 | +0.69 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[CTSZ]] | +0.77 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[FKBP9]] | +0.76 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[ANKRD30BL]] | +0.76 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[RPSA]] | +0.75 | +0.59 / +0.78 | both halves | 7e-06 |  |
| [[HNRNPA3]] | +0.75 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[RPN1]] | +0.74 | +0.58 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[MOB1A]] | +0.74 | +0.54 / +0.76 | both halves | 1e-05 |  |
| [[NONO]] | +0.73 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[EEF1A1]] | +0.73 | +0.62 / +0.72 | both halves | 7e-06 | STRING 436 |
| [[LIN7C]] | +0.73 | +0.43 / +0.77 | both halves | 3e-05 |  |
| [[UBQLN4]] | +0.72 | +0.45 / +0.77 | both halves | 3e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 7 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | -0.77 | -0.54 / -0.80 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL36]] | -0.72 | -0.31 / -0.80 | both halves | 2e-04 |  |
| [[ZNF593]] | -0.72 | -0.44 / -0.79 | both halves | 3e-05 |  |
| [[RPL36AL]] ⚠ | -0.72 | -0.34 / -0.79 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[PIGBOS1]] | -0.70 | -0.54 / -0.74 | both halves | 1e-05 |  |
| [[EMC6]] | -0.70 | -0.26 / -0.81 | both halves | 4e-04 |  |
| [[TRAPPC2B]] | -0.69 | -0.45 / -0.74 | both halves | 3e-05 |  |
| [[NKAP]] | -0.69 | -0.54 / -0.74 | both halves | 1e-05 |  |
| [[MED19]] | -0.69 | -0.51 / -0.72 | both halves | 1e-05 |  |
| [[MRPL46]] | -0.69 | -0.42 / -0.72 | both halves | 4e-05 |  |
| [[ADPRS]] | -0.68 | -0.41 / -0.73 | both halves | 4e-05 |  |
| [[RPP21]] | -0.68 | -0.36 / -0.73 | both halves | 1e-04 |  |
| [[C16orf91]] | -0.68 | -0.31 / -0.75 | both halves | 2e-04 |  |
| [[ZNF503]] | -0.67 | -0.60 / -0.69 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.826). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-28.2, -24.3); signed map (-20.8, -36.2). **Vector** length 116, 30.9% of its response variance represented; |z| ≥ 3 in 700 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cap-dependent Translation Initiation* (reactome, mean cos +0.56 to 12); *Eukaryotic Translation Initiation* (reactome, mean cos +0.56 to 12); *L13a-mediated translational silencing of Ceruloplasmin expression* (reactome, mean cos +0.57 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +13.5 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +13.5 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +13.3 | +10.2 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.9 | +2.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.4 | +3.4 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.3 | +2.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +2.2 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[Folic acid (drug)]] 5 µM |  | +2.1 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.8 | -3.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.5 | -1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -1.9 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -2.2 | -1.7 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.2 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | dihydrofolate reductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1 — chr5:80,626,226-80,654,983 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DHFR1 |
| Gene groups (HGNC) | Dihydrofolate reductase family |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 10 pathways, smallest: Tetrahydrobiopterin (BH4) synthesis, recycling, salvage and regulation; Metabolism of folate and pterines; Metabolism of cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [P00374](https://www.uniprot.org/uniprotkb/P00374) (Dihydrofolate reductase):

> Catalyzes the reduction of 7,8-dihydrofolate (DHF) to 5,6,7,8-tetrahydrofolate in a NADPH-dependent manner. Key enzyme in folate metabolism. Contributes to the nuclear and mitochondrial de novo thymidylate biosynthesis pathway. Catalyzes an essential reaction for de novo glycine and purine synthesis, and for DNA precursor synthesis. Binds its own mRNA and that of DHFR2.

**Summary**, from NCBI Gene [1719](https://www.ncbi.nlm.nih.gov/gene/1719):

> Dihydrofolate reductase converts dihydrofolate into tetrahydrofolate, a methyl group shuttle required for the de novo synthesis of purines, thymidylic acid, and certain amino acids. While the functional dihydrofolate reductase gene has been mapped to chromosome 5, multiple intronless processed pseudogenes or dihydrofolate reductase-like genes have been identified on separate chromosomes. Dihydrofolate reductase deficiency has been linked to megaloblastic anemia. Several transcript variants …

**Accessions** — [HGNC:2861](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2861) · Entrez [1719](https://www.ncbi.nlm.nih.gov/gene/1719) · UniProt [P00374](https://www.uniprot.org/uniprotkb/P00374) · Ensembl [ENSG00000228716](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228716)

## Data

Gene col 13670: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13670); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13670, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13670]; `tensor/DDL_lfc|DDL_z.npy` [13670]; `embed/gene_vectors.npy` [13670]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13670 or target_col == 13670). Every well: [[DHFR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHFR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
