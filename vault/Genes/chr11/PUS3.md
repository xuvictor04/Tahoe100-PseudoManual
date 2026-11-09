---
symbol: "PUS3"
type: "gene"
col: 3108
ensembl_id: "ENSG00000110060"
name: "pseudouridine synthase 3"
location: "11q24.2"
module: 12
arm: "+"
pooled_cpm: 9.61
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# PUS3

*pseudouridine synthase 3* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.44× (z +12.8, q 2e-34, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.664× (z -4.2, q 0.013, down in 18 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SW1417 0.112×, NCI-H2030 0.107×, PANC-1 0.195×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 0.0884×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.0968×; ⚠ cell-cycle shift, explains ~0% of this change); [[Monocrotaline (drug)]] 5 µM in 1 line (HepG2/C3A 0.0589×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.346×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPHOSPH10]] (+0.79, fdr 7e-06), [[C18orf21]] (+0.77, fdr 7e-06), [[NOL7]] (+0.76, fdr 7e-06, ⚠ NOL7 in the vector space only through flagged drug-doses), [[RPP21]] (+0.75, fdr 1e-05); moves opposite to [[MOB1A]] (-0.67, fdr 1e-05), [[CDK2AP1]] (-0.64, fdr 1e-05), [[EDEM1]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3108.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.44×** | +12.8 | 2e-34 | 46/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.41×** | +12.7 | 3e-34 | 47/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.12×** | +11.3 | 2e-27 | 32/35 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.88×** | +10.9 | 1e-25 | 44/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.13×** | +7.8 | 6e-13 | 27/40 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.00×** | +7.2 | 7e-11 | 36/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.62×** | +7.1 | 1e-10 | 26/44 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.90×** | +6.6 | 3e-09 | 26/47 (KATO III, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.94×** | +6.6 | 3e-09 | 29/45 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.84×** | +6.3 | 2e-08 | 30/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.70×** | +5.2 | 1e-05 | 29/45 (KATO III, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +4.8 | 9e-05 | 23/47 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +4.6 | 2e-04 | 24/45 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.55×** | +4.5 | 3e-04 | 19/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.52×** | +4.3 | 6e-04 | 16/39 (HT-29, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.004 | 14/47 (BT-474, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3108.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SW1417 0.112×, NCI-H2030 0.107×, PANC-1 0.195×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 0.0884×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.0968×; ⚠ cell-cycle shift, explains ~0% of this change); [[Monocrotaline (drug)]] 5 µM in 1 line (HepG2/C3A 0.0589×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.346×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.664×** | -4.2 | 0.013 | 18/47 (LS 180, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ferulic acid (drug)]] 0.5 µM |  | 0.728× | -3.3 | 0.27 | 13/46 (KATO III, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.746× | -3.0 | 0.44 | 16/47 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3108. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 15.1 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +10.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.37× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.195× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 14.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.86× (z +9.3) | — |
| [[HepG2_C3A (line)]] | wt | 9.81 | 0 | 1 | — | [[Monocrotaline (drug)]] 5 µM 0.0589× (z -9.5) |
| [[HOP62 (line)]] | alt | 5.61 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0968× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0884× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 9.69 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3108), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 6 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPHOSPH10]] | +0.79 | +0.68 / +0.77 | both halves | 7e-06 |  |
| [[C18orf21]] | +0.77 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[NOL7]] ⚠ | +0.76 | +0.70 / +0.67 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPP21]] | +0.75 | +0.54 / +0.71 | both halves | 1e-05 | pathway: tRNA processing |
| [[NSUN5]] | +0.73 | +0.59 / +0.77 | both halves | 7e-06 | STRING 473 |
| [[RBMX2]] | +0.73 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[CINP]] | +0.73 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[MRPL46]] | +0.71 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[ZNF329]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[POLR2I]] | +0.70 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[PDRG1]] | +0.70 | +0.61 / +0.78 | both halves | 7e-06 |  |
| [[TRAPPC5]] | +0.69 | +0.42 / +0.70 | both halves | 4e-05 |  |
| [[PET117]] | +0.69 | +0.32 / +0.70 | both halves | 2e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | -0.67 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[CDK2AP1]] | -0.64 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[EDEM1]] | -0.63 | -0.44 / -0.72 | both halves | 3e-05 |  |
| [[PRKAR1A]] | -0.62 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[HCFC1]] | -0.60 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[EIF4EBP2]] | -0.60 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[SUMO3]] | -0.59 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[RCC2]] | -0.59 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[CERS2]] | -0.59 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[DHFR]] | -0.58 | -0.32 / -0.58 | both halves | 2e-04 |  |
| [[ATP11C]] | -0.58 | -0.40 / -0.56 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.688). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-38.4, -9.4); signed map (-16.6, -7.9). **Vector** length 78.5, 16.0% of its response variance represented; |z| ≥ 3 in 865 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +4.1 | +7.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.0 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.1 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +11.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +4.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +1.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.1 | +2.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.8 | -1.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.4 | -0.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.0 | -2.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | +0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -0.9 |
|  | [[Encorafenib (drug)]] 5 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | pseudouridine synthase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:125,893,485-125,903,221 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FKSG32, DEG1 |
| Gene groups (HGNC) | Pseudouridine synthases |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZE2](https://www.uniprot.org/uniprotkb/Q9BZE2) (tRNA pseudouridine(38/39) synthase):

> Formation of pseudouridine at position 39 in the anticodon stem and loop of transfer RNAs.

**Summary**, from NCBI Gene [83480](https://www.ncbi.nlm.nih.gov/gene/83480):

> The protein encoded by this gene catalyzes the formation of tRNA pseudouridine from tRNA uridine at position 39 in the anticodon stem and loop of transfer RNAs. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:25461](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25461) · Entrez [83480](https://www.ncbi.nlm.nih.gov/gene/83480) · UniProt [Q9BZE2](https://www.uniprot.org/uniprotkb/Q9BZE2) · Ensembl [ENSG00000110060](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110060)

## Data

Gene col 3108: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3108); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3108, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3108]; `tensor/DDL_lfc|DDL_z.npy` [3108]; `embed/gene_vectors.npy` [3108]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3108 or target_col == 3108). Every well: [[PUS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PUS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
