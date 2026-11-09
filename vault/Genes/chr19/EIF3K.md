---
symbol: "EIF3K"
type: "gene"
col: 10984
ensembl_id: "ENSG00000178982"
name: "eukaryotic translation initiation factor 3 subunit K"
location: "19q13.2"
module: 7
arm: "-"
pooled_cpm: 73.58
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# EIF3K

*eukaryotic translation initiation factor 3 subunit K* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.02× (z +11.5, q 1e-27, up in 47 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 13 lines (NCI-H460 4.36×, RKO 4.17×, MIA PaCa-2 4.54×, NCI-H1792 4.95×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 4.59×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 4.09×; ⚠ toxic; cell-cycle shift, explains ~19% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.728× (z -4.6, q 0.002, down in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.311×, H4 0.356×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNRPD2]] (+0.73, fdr 7e-06), [[UQCRH]] (+0.72, fdr 7e-06), [[RPS21]] (+0.66, fdr 1e-05); moves opposite to [[EIF4G2]] (-0.65, fdr 2e-05), [[BMI1]] (-0.64, fdr 1e-05), [[HMGN2]] (-0.63, fdr 2e-05).
> It sits in the **-** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10984.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 13 lines (NCI-H460 4.36×, RKO 4.17×, MIA PaCa-2 4.54×, NCI-H1792 4.95×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 4.59×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 4.09×; ⚠ toxic; cell-cycle shift, explains ~19% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.02×** | +11.5 | 1e-27 | 47/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.33×** | +8.4 | 1e-14 | 39/40 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.05×** | +6.9 | 1e-09 | 40/45 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.40×** | +3.5 | 0.072 | 30/46 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10984.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.311×, H4 0.356×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.728×** | -4.6 | 0.002 | 33/48 (A-427, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.731× | -3.1 | 0.42 | 24/47 (C32, RKO, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.525× | -3.1 | 0.42 | 29/49 (A-427, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10984. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 51.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-427 (line)]] | wt | 71.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -13.0) |
| [[HOP62 (line)]] | alt | 55.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW480 (line)]] | alt | 50.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.59× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 43.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A498 (line)]] | wt | 64.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A549 (line)]] | wt | 105 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[C32 (line)]] | wt | 34.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[H4 (line)]] | wt | 86.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -10.1) |
| [[HT-29 (line)]] | alt | 86.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[LoVo (line)]] | wt | 61.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[LOX-IMVI (line)]] | wt | 57.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 50.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1573 (line)]] | alt | 29.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1792 (line)]] | alt | 44.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H460 (line)]] | wt | 41.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[PANC-1 (line)]] | alt | 415 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW 900 (line)]] | alt | 43.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[AN3 CA (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 61.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10984), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPD2]] | +0.73 | +0.65 / +0.60 | both halves | 7e-06 | STRING 536 |
| [[UQCRH]] | +0.72 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[RPS21]] | +0.66 | +0.55 / +0.58 | both halves | 1e-05 | pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 980 |
| [[NAA10]] ⚠ | +0.65 | +0.41 / +0.54 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS5]] | +0.64 | +0.49 / +0.53 | both halves | 1e-05 | pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 963 |
| [[TYW1]] | +0.64 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[DAP3]] | +0.63 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[NAT9]] | +0.62 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[RPS25]] | +0.62 | +0.49 / +0.53 | both halves | 1e-05 | pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 973 |
| [[NAA35]] | +0.62 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[MICOS13]] | +0.61 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[RPL27A]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 | pathway: Cap-dependent Translation Initiation |
| [[SDF2L1]] | +0.61 | +0.53 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.65 | -0.46 / -0.53 | both halves | 2e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[BMI1]] | -0.64 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[HMGN2]] | -0.63 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[WAC-AS1]] | -0.63 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[CDC42EP1]] | -0.63 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[ZNF564]] | -0.62 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[DDX6]] | -0.61 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[CGGBP1]] | -0.60 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[RIPK2-DT]] | -0.60 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[CFL2]] | -0.60 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[ZBED5-AS1]] | -0.59 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[ZNF606]] | -0.59 | -0.53 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **-** arm (projection on the module's main direction -0.302). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-48.7, -25.6); signed map (-56.4, -3.4). **Vector** length 58.3, 15.7% of its response variance represented; |z| ≥ 3 in 513 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +2.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +2.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +2.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.0 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | -0.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.3 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.0 | +0.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.3 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | -2.9 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -2.8 | +8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | +0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | -0.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.3 | -0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 3 subunit K |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:38,619,082-38,636,955 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRO1474, HSPC029, PTD001, PLAC-24, M9, ARG134; previously EIF3S12 |
| Gene groups (HGNC) | Eukaryotic translation initiation factor 3 complex subunits |
| Reactome | 14 pathways, smallest: Formation of the ternary complex, and subsequently, the 43S complex; Ribosomal scanning and start codon recognition; Translation initiation complex formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBQ5](https://www.uniprot.org/uniprotkb/Q9UBQ5) (Eukaryotic translation initiation factor 3 subunit K):

> Component of the eukaryotic translation initiation factor 3 (eIF-3) complex, which is required for several steps in the initiation of protein synthesis. The eIF-3 complex associates with the 40S ribosome and facilitates the recruitment of eIF-1, eIF-1A, eIF-2:GTP:methionyl-tRNAi and eIF-5 to form the 43S pre-initiation complex (43S PIC). The eIF-3 complex stimulates mRNA recruitment to the 43S PIC and scanning of the mRNA for AUG recognition. The eIF-3 complex is also required for disassembly …

**Summary**, from NCBI Gene [27335](https://www.ncbi.nlm.nih.gov/gene/27335):

> The 700-kD eukaryotic translation initiation factor-3 (eIF3) is the largest eIF and contains at least 12 subunits, including EIF2S12. eIF3 plays an essential role in translation by binding directly to the 40S ribosomal subunit and promoting formation of the 40S preinitiation complex (Mayeur et al., 2003 [PubMed 14519125]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:24656](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24656) · Entrez [27335](https://www.ncbi.nlm.nih.gov/gene/27335) · UniProt [Q9UBQ5](https://www.uniprot.org/uniprotkb/Q9UBQ5) · Ensembl [ENSG00000178982](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178982)

## Data

Gene col 10984: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10984); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10984, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10984]; `tensor/DDL_lfc|DDL_z.npy` [10984]; `embed/gene_vectors.npy` [10984]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10984 or target_col == 10984). Every well: [[EIF3K — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF3K.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
