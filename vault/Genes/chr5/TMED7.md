---
symbol: "TMED7"
type: "gene"
col: 5630
ensembl_id: "ENSG00000134970"
name: "transmembrane p24 trafficking protein 7"
location: "5q22.3"
module: 20
arm: "+"
pooled_cpm: 82.15
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# TMED7

*transmembrane p24 trafficking protein 7* — 5q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 1.72× (z +7.2, q 2e-10, up in 36 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.32× (z +6.4, q 4e-08, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.636× (z -9.2, q 2e-17, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMED2]] (+0.80, fdr 7e-06), [[BPNT2]] (+0.78, fdr 7e-06), [[TMEM30A]] (+0.76, fdr 7e-06); moves opposite to [[WBP4]] (-0.67, fdr 7e-06), [[CROCCP2-1]] (-0.66, fdr 7e-06), [[EIF4EBP3]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EID2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5630.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +7.2 | 2e-10 | 36/45 (NCI-H1573, SW480, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.61×** | +6.8 | 2e-09 | 34/49 (NCI-H1573, HOP62, …) | all doses, flat | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.32×** | +6.4 | 4e-08 | 43/49 (NCI-H1573, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.50×** | +5.6 | 3e-06 | 28/43 (A549, HOP62, …) | all doses, flat | composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +4.9 | 1e-04 | 36/48 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +4.9 | 1e-04 | 31/48 (AsPC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.81×** | +4.5 | 7e-04 | 25/37 (NCI-H1573, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.3 | 0.001 | 0/50 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +4.2 | 0.001 | 31/48 (NCI-H1573, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +3.3 | 0.048 | 20/48 (NCI-H1792, HOP62, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.071 | 26/48 (C-33 A, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~17% of this change | 1.24× | +3.0 | 0.11 | 20/48 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5630.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.636×** | -9.2 | 2e-17 | 37/48 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.698×** | -5.0 | 1e-04 | 30/48 (LoVo, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.726×** | -4.7 | 5e-04 | 37/48 (KATO III, LoVo, …) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.640×** | -4.6 | 5e-04 | 37/48 (CHP-212, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **0.781×** | -3.6 | 0.036 | 30/48 (A-172, LOX-IMVI, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.781×** | -3.5 | 0.050 | 22/47 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.793×** | -3.4 | 0.057 | 28/48 (HCT15, SW1417, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 0.813× | -3.0 | 0.16 | 21/48 (SW480, NCI-H2347, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.813× | -3.0 | 0.16 | 22/48 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5630. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 90.6 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +15.2) | — |
| [[AsPC-1 (line)]] | alt | 168 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.79× (z +16.5) | — |
| [[HOP62 (line)]] | alt | 86.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -11.3) |
| [[A549 (line)]] | wt | 69.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2030 (line)]] | alt | 60.2 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 142 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -15.5) |
| [[SW480 (line)]] | alt | 66.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.73× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 73.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 60.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.232× (z -11.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 142 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -9.1) |
| [[HS-578T (line)]] | alt | 142 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -8.9) |
| [[HT-29 (line)]] | alt | 85.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.362× (z -9.5) ⚠ toxic |
| [[J82 (line)]] | alt | 91.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -10.6) |
| [[KATO III (line)]] | alt | 69.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -8.9) |
| [[LoVo (line)]] | wt | 105 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.420× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 68.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 114 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -12.5) |
| [[NCI-H661 (line)]] | alt | 60.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -9.0) |
| [[PANC-1 (line)]] | alt | 71.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -10.6) |
| [[RKO (line)]] | wt | 70.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 85.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -9.9) |
| [[SHP-77 (line)]] | alt | 50.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.08× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 83.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[SNU-1 (line)]] | wt | 82.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -8.9) |
| [[A-172 (line)]] | wt | 77.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 83.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 97.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 100 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 94.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 66.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 97.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 74.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5630), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED2]] | +0.80 | +0.72 / +0.81 | both halves | 7e-06 | same gene group; pathway: Asparagine N-linked glycosylation; STRING 969 |
| [[BPNT2]] | +0.78 | +0.76 / +0.81 | both halves | 7e-06 |  |
| [[TMEM30A]] | +0.76 | +0.71 / +0.80 | both halves | 7e-06 | STRING 450 |
| [[TXNDC5]] | +0.75 | +0.75 / +0.81 | both halves | 7e-06 |  |
| [[RPN1]] | +0.75 | +0.77 / +0.84 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[DNAJB11]] | +0.74 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[STT3A]] | +0.73 | +0.69 / +0.76 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[FAM91A1]] | +0.71 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[SSR1]] | +0.71 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[UGGT1]] | +0.70 | +0.60 / +0.69 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[ARF1]] | +0.70 | +0.68 / +0.85 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 619 |
| [[DDOST]] | +0.70 | +0.73 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WBP4]] | -0.67 | -0.69 / -0.60 | both halves | 7e-06 |  |
| [[CROCCP2-1]] | -0.66 | -0.62 / -0.73 | both halves | 7e-06 |  |
| [[EIF4EBP3]] | -0.64 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[UNK]] | -0.63 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[FDX2]] | -0.63 | -0.57 / -0.63 | both halves | 8e-06 |  |
| [[RBX1]] | -0.63 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[TOPORS]] | -0.63 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[SEMA4C]] | -0.63 | -0.39 / -0.59 | both halves | 5e-05 |  |
| [[CHKB]] | -0.63 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[ZCCHC10]] | -0.63 | -0.49 / -0.68 | both halves | 1e-05 |  |
| [[ZCCHC3]] | -0.62 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[CDK3]] | -0.62 | -0.67 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EID2]] | C | EID2 activity lowers TMED7's level | lines that do not express EID2 (3) vs lines expressing it (47) | 1.97× higher at baseline in the lines without EID2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.717). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-24.3, -22.7); signed map (-24.3, -39.8). **Vector** length 122, 36.3% of its response variance represented; |z| ≥ 3 in 956 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Maturation of DENV proteins* (reactome, mean cos +0.59 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +5.7 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +5.5 | +5.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +4.9 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +2.5 | +2.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +2.3 | +0.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.8 | -9.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.2 | -5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.2 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.1 | -3.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.3 | -2.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.8 | -1.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.8 | -4.7 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane p24 trafficking protein 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q22.3 — chr5:115,613,210-115,632,992 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-109, FLJ90481, p24gamma3, p24g3 |
| Gene groups (HGNC) | Transmembrane p24 trafficking proteins |
| Reactome | 9 pathways, smallest: COPI-dependent Golgi-to-ER retrograde traffic; COPI-mediated anterograde transport; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3B3](https://www.uniprot.org/uniprotkb/Q9Y3B3) (Transmembrane emp24 domain-containing protein 7):

> Potential role in vesicular protein trafficking, mainly in the early secretory pathway. Appears to play a role in the biosynthesis of secreted cargo including processing and post-translational modifications.

**Summary**, from NCBI Gene [51014](https://www.ncbi.nlm.nih.gov/gene/51014):

> Predicted to be involved in Golgi organization; endoplasmic reticulum to Golgi vesicle-mediated transport; and intracellular protein transport. Located in Golgi apparatus; endoplasmic reticulum; and endoplasmic reticulum-Golgi intermediate compartment. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24253](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24253) · Entrez [51014](https://www.ncbi.nlm.nih.gov/gene/51014) · UniProt [Q9Y3B3](https://www.uniprot.org/uniprotkb/Q9Y3B3) · Ensembl [ENSG00000134970](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134970)

## Data

Gene col 5630: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5630); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5630, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5630]; `tensor/DDL_lfc|DDL_z.npy` [5630]; `embed/gene_vectors.npy` [5630]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5630 or target_col == 5630). Every well: [[TMED7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMED7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
