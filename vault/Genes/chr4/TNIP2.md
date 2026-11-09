---
symbol: "TNIP2"
type: "gene"
col: 9715
ensembl_id: "ENSG00000168884"
name: "TNFAIP3 interacting protein 2"
location: "4p16.3"
module: 20
arm: "-"
pooled_cpm: 29.09
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# TNIP2

*TNFAIP3 interacting protein 2* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.12× (z +17.3, q 0e+00, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.653× (z -9.8, q 5e-20, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RELA]] (+0.64, fdr 1e-05), [[ZNF23]] (+0.63, fdr 1e-05), [[NSUN5]] (+0.63, fdr 1e-05); moves opposite to [[RBBP4]] (-0.59, fdr 1e-05), [[RPN2]] (-0.58, fdr 1e-05), [[FUCA2]] (-0.57, fdr 4e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9715.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.12×** | +17.3 | 0e+00 | 32/47 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.05×** | +11.3 | 6e-27 | 34/47 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +10.5 | 2e-23 | 29/47 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.65×** | +7.2 | 6e-11 | 37/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +6.2 | 5e-08 | 33/48 (A-172, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.39×** | +5.4 | 6e-06 | 23/45 (J82, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +4.6 | 3e-04 | 19/48 (PANC-1, Panc 03.27, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.35×** | +4.5 | 6e-04 | 20/45 (HS-578T, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.31×** | +4.4 | 7e-04 | 19/48 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.66×** | +4.3 | 9e-04 | 20/46 (CFPAC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.29×** | +4.1 | 0.002 | 19/48 (KATO III, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.40×** | +3.9 | 0.004 | 22/47 (Panc 03.27, SW480, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.005 | 17/46 (NCI-H1573, A498, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.009 | 15/46 (SW1417, SW480, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.6 | 0.013 | 15/44 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.035 | 17/48 (SW480, A498, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.048 | 14/42 (CFPAC-1, H4, …) | two highest doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.065 | 15/47 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9715.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.653×** | -9.8 | 5e-20 | 35/47 (Panc 03.27, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -6.2 | 2e-07 | 27/47 (SW480, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.780×** | -3.9 | 0.018 | 19/48 (A-172, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 0.850× | -3.7 | 0.025 | 18/48 (H4, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Tofacitinib (drug)]] 5 µM |  | 0.855× | -3.6 | 0.034 | 18/48 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | 0.697× | -3.1 | 0.19 | 13/46 (SW48, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9715. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 41.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +20.1) | — |
| [[PANC-1 (line)]] | alt | 32.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +12.9) | — |
| [[A-172 (line)]] | wt | 58.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +21.1) | — |
| [[A549 (line)]] | wt | 35.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +16.8) | — |
| [[NCI-H460 (line)]] | wt | 22.7 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.76× (z +12.8) | — |
| [[HOP62 (line)]] | alt | 28.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +21.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +14.3) | — |
| [[NCI-H1573 (line)]] | alt | 42.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +15.8) | — |
| [[CFPAC-1 (line)]] | alt | 59.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 25.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +11.6) | [[Hydroxyfasudil (drug)]] 5 µM 0.0581× (z -8.7) |
| [[J82 (line)]] | alt | 57.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +20.0) | — |
| [[LOX-IMVI (line)]] | wt | 37.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.334× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 34.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -9.0) |
| [[SNU-423 (line)]] | alt | 22.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +19.2) | — |
| [[A-427 (line)]] | wt | 23.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 43.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -8.6) |
| [[CHP-212 (line)]] | wt | 28.1 | 0 | 1 | — | [[Triclosan (drug)]] 0.5 µM 0.0762× (z -8.9) |
| [[Hs 766T (line)]] | wt | 41.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0785× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 22.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 24.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.238× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~50% of this change |
| [[NCI-H2347 (line)]] | alt | 41.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 34.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -10.2) |
| [[RKO (line)]] | wt | 28.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +13.9) | — |
| [[RPMI-7951 (line)]] | alt | 17.3 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.164× (z -8.9) |
| [[SW 900 (line)]] | alt | 14.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +12.4) | — |
| [[SW1417 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9715), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RELA]] | +0.64 | +0.55 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 836 |
| [[ZNF23]] | +0.63 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[NSUN5]] | +0.63 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[SURF2]] | +0.62 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[N4BP3]] | +0.62 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[MAP1S]] | +0.60 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[LRRC8E]] | +0.59 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[SMIM29]] | +0.59 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[ARRDC2]] | +0.58 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[GLRX2]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[RHOG]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[TIPRL]] | +0.57 | +0.51 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP4]] | -0.59 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[RPN2]] | -0.58 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[FUCA2]] | -0.57 | -0.55 / -0.40 | both halves | 4e-05 |  |
| [[DDOST]] | -0.57 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[PDIA3]] | -0.56 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[PHTF2]] | -0.56 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[PRDM10]] | -0.55 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[STT3B]] | -0.55 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[TMED4]] | -0.55 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[RCN2]] | -0.54 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[SUMO3]] | -0.54 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[LAMTOR5-AS1]] | -0.54 | -0.38 / -0.49 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TNIP2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 0.8% of all compounds | 0.010 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[RAPGEF4]] | B | RAPGEF4 activity lowers TNIP2's level | lines that do not express RAPGEF4 (5) vs lines expressing it (45) | 1.42× higher at baseline in the lines without RAPGEF4 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000286739, BIVM, CLIP3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.464). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.5, -3.6); signed map (-16.1, -6.5). **Vector** length 105, 25.3% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.6 | +17.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.1 | +11.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.2 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +10.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.7 | +4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.5 | +4.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.1 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.8 | +3.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -9.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -1.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -2.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.0 | -3.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | TNFAIP3 interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:2,741,648-2,756,342 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ABIN-2, MGC4289, KLIP, FLIP1, ABIN2 |
| Gene groups (HGNC) | Zinc fingers C2HC NEMO-type |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 26 pathways, smallest: MAP3K8 (TPL2)-dependent MAPK1/3 activation; Ovarian tumor domain proteases; MAP kinase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFZ5](https://www.uniprot.org/uniprotkb/Q8NFZ5) (TNFAIP3-interacting protein 2):

> Inhibits NF-kappa-B activation by blocking the interaction of RIPK1 with its downstream effector NEMO/IKBKG. Forms a ternary complex with NFKB1 and MAP3K8 but appears to function upstream of MAP3K8 in the TLR4 signaling pathway that regulates MAP3K8 activation. Involved in activation of the MEK/ERK signaling pathway during innate immune response; this function seems to be stimulus- and cell type specific. Required for stability of MAP3K8. Involved in regulation of apoptosis in endothelial …

**Summary**, from NCBI Gene [79155](https://www.ncbi.nlm.nih.gov/gene/79155):

> This gene encodes a protein which acts as an inhibitor of NFkappaB activation. The encoded protein is also involved in MAP/ERK signaling pathway in specific cell types. It may be involved in apoptosis of endothelial cells. Alternative splicing results in multiple transcript variants. A pseudogene related to this gene is located on the X chromosome.[provided by RefSeq, May 2014]

**Accessions** — [HGNC:19118](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19118) · Entrez [79155](https://www.ncbi.nlm.nih.gov/gene/79155) · UniProt [Q8NFZ5](https://www.uniprot.org/uniprotkb/Q8NFZ5) · Ensembl [ENSG00000168884](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168884)

## Data

Gene col 9715: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9715); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9715, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9715]; `tensor/DDL_lfc|DDL_z.npy` [9715]; `embed/gene_vectors.npy` [9715]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9715 or target_col == 9715). Every well: [[TNIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
