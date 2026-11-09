---
symbol: "CDK5RAP2"
type: "gene"
col: 5921
ensembl_id: "ENSG00000136861"
name: "CDK5 regulatory subunit associated protein 2"
location: "9q33.2"
module: 6
arm: "+"
pooled_cpm: 145.99
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 29
n_dd_up_clean: 0
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CDK5RAP2

*CDK5 regulatory subunit associated protein 2* — 9q33.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.402× (z -30.8, q 0e+00, down in 48 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUBGCP3]] (+0.83, fdr 7e-06), [[TIMELESS]] (+0.69, fdr 7e-06), [[CCDC150]] (+0.69, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5921.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.4 | 0.39 | 17/47 (NCI-H23, A549, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.27× | +3.0 | 0.69 | 15/49 (Panc 03.27, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5921.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.402×** | -30.8 | 0e+00 | 48/49 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.658×** | -14.2 | 5e-43 | 38/48 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.568×** | -13.0 | 2e-36 | 43/47 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.596×** | -11.9 | 1e-30 | 42/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.649×** | -10.3 | 6e-23 | 39/48 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.657×** | -10.0 | 1e-21 | 43/48 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.648×** | -10.0 | 2e-21 | 39/50 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.747×** | -9.9 | 4e-21 | 43/48 (A-172, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.667×** | -9.7 | 2e-20 | 43/48 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.675×** | -9.4 | 3e-19 | 42/48 (SW480, SNU-423, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.761×** | -9.2 | 2e-18 | 33/48 (J82, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.729×** | -7.6 | 2e-12 | 32/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.730×** | -7.5 | 2e-12 | 37/48 (J82, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.765×** | -6.4 | 6e-09 | 38/49 (LS 180, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.772×** | -6.2 | 2e-08 | 26/48 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.778×** | -6.0 | 6e-08 | 31/48 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5921. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 169 | 0 | 11 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -26.3) |
| [[J82 (line)]] | alt | 242 | 0 | 10 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -22.0) |
| [[A-172 (line)]] | wt | 185 | 0 | 8 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -20.2) |
| [[LS 180 (line)]] | wt | 116 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -23.2) |
| [[SW480 (line)]] | alt | 212 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -29.0) |
| [[HEC-1-A (line)]] | alt | 277 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -26.4) |
| [[SK-MEL-2 (line)]] | alt | 149 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -15.0) |
| [[A-427 (line)]] | wt | 121 | 0 | 5 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.545× (z -10.4) |
| [[A498 (line)]] | wt | 152 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -23.7) |
| [[HT-29 (line)]] | alt | 94.8 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -21.0) |
| [[SW1417 (line)]] | alt | 139 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -19.2) |
| [[AN3 CA (line)]] | alt | 195 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.225× (z -12.4) |
| [[C32 (line)]] | wt | 143 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -18.7) |
| [[HOP62 (line)]] | alt | 110 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -19.1) |
| [[KATO III (line)]] | alt | 128 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -16.8) |
| [[LOX-IMVI (line)]] | wt | 168 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -29.1) |
| [[MIA PaCa-2 (line)]] | alt | 182 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -21.7) |
| [[Panc 03.27 (line)]] | alt | 116 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -17.8) |
| [[RKO (line)]] | wt | 221 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -25.3) |
| [[RPMI-7951 (line)]] | alt | 129 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -16.0) |
| [[SNU-423 (line)]] | alt | 158 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -21.1) |
| [[H4 (line)]] | wt | 124 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -16.1) |
| [[NCI-H1792 (line)]] | alt | 121 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -19.9) |
| [[NCI-H2030 (line)]] | alt | 117 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -13.2) |
| [[PANC-1 (line)]] | alt | 112 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -20.7) |
| [[SW 900 (line)]] | alt | 105 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -15.7) |
| [[SW48 (line)]] | wt | 151 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 73.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -13.4) |
| [[COLO 205 (line)]] | alt | 158 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -14.6) |
| [[HCT15 (line)]] | alt | 149 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -12.3) |
| [[HepG2_C3A (line)]] | wt | 152 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -14.6) |
| [[Hs 766T (line)]] | wt | 184 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -23.4) |
| [[hTERT-HPNE (line)]] | wt | 85.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -13.1) |
| [[LoVo (line)]] | wt | 95.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -16.3) |
| [[NCI-H23 (line)]] | alt | 160 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -14.3) |
| [[SHP-77 (line)]] | alt | 251 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -12.6) |
| [[SNU-1 (line)]] | wt | 202 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -13.8) |
| [[SW 1271 (line)]] | alt | 256 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.216× (z -10.9) |
| [[A549 (line)]] | wt | 128 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -20.8) |
| [[BT-474 (line)]] | alt | 205 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.589× (z -9.0) |
| [[C-33 A (line)]] | alt | 191 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -13.4) |
| [[CFPAC-1 (line)]] | alt | 61.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -11.3) |
| [[HS-578T (line)]] | alt | 77.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -13.4) |
| [[NCI-H1573 (line)]] | alt | 87.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -10.4) |
| [[NCI-H596 (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.136× (z -8.6) ⚠ cell-cycle shift, explains ~20% of this change |
| [[CHP-212 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 104 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5921), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBGCP3]] | +0.83 | +0.80 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 741 |
| [[TIMELESS]] | +0.69 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[CCDC150]] | +0.69 | +0.79 / +0.54 | both halves | 1e-05 |  |
| [[FANCG]] | +0.68 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[CKAP5]] | +0.68 | +0.59 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 685 |
| [[WDHD1]] | +0.68 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[POLQ]] | +0.68 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[KIF15]] | +0.67 | +0.59 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[NCAPD3]] | +0.67 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[BUB1B]] | +0.67 | +0.60 / +0.68 | both halves | 7e-06 | pathway: Mitotic Prometaphase |
| [[MAD2L1]] | +0.67 | +0.60 / +0.68 | both halves | 7e-06 | pathway: Mitotic Prometaphase |
| [[PBK]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-31.8, -47.9); signed map (-39.1, -40.7). **Vector** length 120, 40.6% of its response variance represented; |z| ≥ 3 in 1,283 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.50 to 28); *Cell Cycle Checkpoints* (reactome, mean cos +0.51 to 45); *Activation of the pre-replicative complex* (reactome, mean cos +0.51 to 22).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.6 | -1.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +8.2 | -3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change | +4.5 | -3.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.3 | -10.3 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.3 | +1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | -0.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.3 | -9.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.2 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | -9.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.6 | -9.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | -3.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.7 | -3.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.6 | -1.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | CDK5 regulatory subunit associated protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.2 — chr9:120,388,875-120,580,170 (-) |
| Ensembl biotype | protein_coding |
| Also known as | C48, FLJ10867, CEP215; previously MCPH3 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96SN8](https://www.uniprot.org/uniprotkb/Q96SN8) (CDK5 regulatory subunit-associated protein 2):

> Potential regulator of CDK5 activity via its interaction with CDK5R1. Negative regulator of centriole disengagement (licensing) which maintains centriole engagement and cohesion. Involved in regulation of mitotic spindle orientation (By similarity). Plays a role in the spindle checkpoint activation by acting as a transcriptional regulator of both BUBR1 and MAD2 promoter. Together with EB1/MAPRE1, may promote microtubule polymerization, bundle formation, growth and dynamics at the plus ends. …

**Summary**, from NCBI Gene [55755](https://www.ncbi.nlm.nih.gov/gene/55755):

> This gene encodes a regulator of CDK5 (cyclin-dependent kinase 5) activity. The protein encoded by this gene is localized to the centrosome and Golgi complex, interacts with CDK5R1 and pericentrin (PCNT), plays a role in centriole engagement and microtubule nucleation, and has been linked to primary microcephaly and Alzheimer's disease. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2013]

**Accessions** — [HGNC:18672](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18672) · Entrez [55755](https://www.ncbi.nlm.nih.gov/gene/55755) · UniProt [Q96SN8](https://www.uniprot.org/uniprotkb/Q96SN8) · Ensembl [ENSG00000136861](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136861)

## Data

Gene col 5921: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5921); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5921, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5921]; `tensor/DDL_lfc|DDL_z.npy` [5921]; `embed/gene_vectors.npy` [5921]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5921 or target_col == 5921). Every well: [[CDK5RAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK5RAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
