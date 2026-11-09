---
symbol: "RBX1"
type: "gene"
col: 1946
ensembl_id: "ENSG00000100387"
name: "ring-box 1"
location: "22q13.2"
module: 20
arm: "-"
pooled_cpm: 56.91
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 15
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# RBX1

*ring-box 1* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.51× (z +5.6, q 1e-05, up in 29 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.384× (z -12.9, q 3e-35, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNK]] (+0.73, fdr 7e-06), [[AK6]] (+0.72, fdr 7e-06), [[LRCH3]] (+0.71, fdr 7e-06); moves opposite to [[AGO1]] (-0.71, fdr 1e-05), [[APP]] (-0.66, fdr 1e-05), [[RPL3]] (-0.65, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1946.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.51×** | +5.6 | 1e-05 | 29/48 (SNU-1, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.31×** | +3.6 | 0.067 | 27/48 (SNU-1, PANC-1, …) | rises with dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.6 | 0.067 | 26/48 (KATO III, HS-578T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.29×** | +3.4 | 0.077 | 24/48 (NCI-H1792, SNU-1, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.4 | 0.077 | 23/47 (SNU-1, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.18 | 10/49 (NCI-H1792, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1946.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.384×** | -12.9 | 3e-35 | 48/48 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.401×** | -12.3 | 2e-32 | 47/48 (HS-578T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.429×** | -11.4 | 8e-28 | 46/48 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.546×** | -8.2 | 5e-14 | 47/48 (HS-578T, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.765×** | -5.1 | 4e-05 | 35/48 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.411×** | -4.7 | 2e-04 | 40/49 (A498, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.793×** | -4.4 | 9e-04 | 25/48 (Panc 03.27, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.749×** | -3.9 | 0.007 | 27/48 (HS-578T, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.763×** | -3.6 | 0.018 | 29/48 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.749×** | -3.6 | 0.019 | 26/48 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.756×** | -3.5 | 0.027 | 27/48 (NCI-H460, SHP-77, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.774×** | -3.4 | 0.028 | 24/48 (SK-MEL-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.769×** | -3.3 | 0.047 | 23/48 (PANC-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.770×** | -3.2 | 0.047 | 25/48 (SW480, HS-578T, …) | inconsistent across doses |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **0.774×** | -3.2 | 0.055 | 23/48 (NCI-H23, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1946. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 68.5 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -10.4) |
| [[HS-578T (line)]] | alt | 97.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.242× (z -14.8) |
| [[SK-MEL-2 (line)]] | alt | 150 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.298× (z -11.5) |
| [[A-172 (line)]] | wt | 51.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.290× (z -10.7) |
| [[A498 (line)]] | wt | 70.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.299× (z -12.8) |
| [[C32 (line)]] | wt | 96.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.313× (z -11.6) |
| [[HOP62 (line)]] | alt | 45.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.294× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 39.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.330× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 56.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.238× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 46.7 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.396× (z -10.7) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.284× (z -10.3) |
| [[PANC-1 (line)]] | alt | 59.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.357× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 42.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 56.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.248× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 73.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.365× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 81.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.391× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 69.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.335× (z -9.0) |
| [[C-33 A (line)]] | alt | 59.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 52.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.355× (z -8.6) |
| [[KATO III (line)]] | alt | 65.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.364× (z -9.1) |
| [[LoVo (line)]] | wt | 52.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.396× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 45.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.345× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 43.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.361× (z -9.8) |
| [[RKO (line)]] | wt | 52.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 48.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.349× (z -8.7) |
| [[SW 1088 (line)]] | alt | 77.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0749× (z -9.0) |
| [[SW 900 (line)]] | alt | 50.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.306× (z -9.1) |
| [[A-427 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 70.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 61.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1946), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNK]] | +0.73 | +0.66 / +0.65 | both halves | 7e-06 | same gene group |
| [[AK6]] | +0.72 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[LRCH3]] | +0.71 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[NDUFA13]] ⚠ | +0.70 | +0.59 / +0.74 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ZCCHC10]] | +0.69 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[TOPORS]] | +0.69 | +0.50 / +0.70 | both halves | 1e-05 | same gene group |
| [[NDUFC1]] | +0.69 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[GGA3]] | +0.66 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[TERF2IP]] | +0.65 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[NDUFA6]] | +0.65 | +0.47 / +0.70 | both halves | 2e-05 |  |
| [[CHKB]] | +0.65 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[PDCD7]] | +0.65 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[FAM193A]] | +0.65 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGO1]] | -0.71 | -0.50 / -0.71 | both halves | 1e-05 | pathway: Co-inhibition by PD-1 |
| [[APP]] | -0.66 | -0.57 / -0.75 | both halves | 1e-05 | pathway: Interleukin-1 family signaling |
| [[RPL3]] | -0.65 | -0.56 / -0.63 | both halves | 1e-05 | pathway: Regulation of expression of SLITs and ROBOs |
| [[NDRG3]] | -0.64 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[RPSA]] | -0.64 | -0.58 / -0.64 | both halves | 7e-06 | pathway: Regulation of expression of SLITs and ROBOs |
| [[ERMP1]] | -0.64 | -0.57 / -0.61 | both halves | 8e-06 |  |
| [[MAT2A]] | -0.63 | -0.61 / -0.67 | both halves | 7e-06 |  |
| [[YWHAQ]] | -0.63 | -0.60 / -0.65 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[PRELID3B]] | -0.63 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[TMED7]] | -0.63 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[SPTBN1]] | -0.63 | -0.54 / -0.61 | both halves | 1e-05 | pathway: MAPK family signaling cascades |
| [[NONO]] | -0.62 | -0.54 / -0.68 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.672). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-26.8, -24.2); signed map (-2.0, -8.3). **Vector** length 99.3, 31.0% of its response variance represented; |z| ≥ 3 in 667 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +6.5 | +1.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | -0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +4.3 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.3 | +2.9 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +2.1 | +2.9 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.9 | +1.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.5 | -1.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.6 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.2 | -8.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.1 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | ring-box 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:40,951,347-40,973,309 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ROC1, RNF75, BA554C12.1 |
| Gene groups (HGNC) | Ring finger proteins; SCF complex core subunits; RING finger E3 ubiquitin protein ligases; Degenerate RING E3 ubiquitin ligases |
| Hallmark sets | NOTCH_SIGNALING, DNA_REPAIR |
| Reactome | 103 pathways, smallest: FBXW7 Mutants and NOTCH1 in Cancer; Loss of Function of FBXW7 in Cancer and NOTCH1 Signaling; Prolactin receptor signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P62877](https://www.uniprot.org/uniprotkb/P62877) (E3 ubiquitin-protein ligase RBX1):

> E3 ubiquitin ligase component of multiple cullin-RING-based E3 ubiquitin-protein ligase (CRLs) complexes which mediate the ubiquitination and subsequent proteasomal degradation of target proteins, including proteins involved in cell cycle progression, signal transduction, transcription and transcription-coupled nucleotide excision repair. CRLs complexes and ARIH1 collaborate in tandem to mediate ubiquitination of target proteins, ARIH1 mediating addition of the first ubiquitin on CRLs targets. …

**Summary**, from NCBI Gene [9978](https://www.ncbi.nlm.nih.gov/gene/9978):

> This locus encodes a RING finger-like domain-containing protein. The encoded protein interacts with cullin proteins and likely plays a role in ubiquitination processes necessary for cell cycle progression. This protein may also affect protein turnover. Related pseudogenes exist on chromosomes 2 and 5.[provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:9928](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9928) · Entrez [9978](https://www.ncbi.nlm.nih.gov/gene/9978) · UniProt [P62877](https://www.uniprot.org/uniprotkb/P62877) · Ensembl [ENSG00000100387](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100387)

## Data

Gene col 1946: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1946); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1946, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1946]; `tensor/DDL_lfc|DDL_z.npy` [1946]; `embed/gene_vectors.npy` [1946]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1946 or target_col == 1946). Every well: [[RBX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
