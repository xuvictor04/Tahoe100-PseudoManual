---
symbol: "MCM3AP-AS1"
type: "gene"
col: 13264
ensembl_id: "ENSG00000215424"
name: "MCM3AP antisense RNA 1"
location: "21q22.3"
module: 18
arm: "+"
pooled_cpm: 11.94
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# MCM3AP-AS1

*MCM3AP antisense RNA 1* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.47× (z +6.4, q 1e-07, up in 23 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.451× (z -18.6, q 0e+00, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GARNL3]] (+0.64, fdr 7e-06), [[SLC29A2]] (+0.64, fdr 7e-06), [[SFXN4]] (+0.63, fdr 7e-06); moves opposite to [[SYNJ1]] (-0.57, fdr 1e-05), [[SMIM14]] (-0.54, fdr 2e-05), [[USP11]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FAM78B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13264.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +6.4 | 1e-07 | 23/46 (HT-29, CFPAC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.6 | 0.001 | 12/39 (NCI-H23, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.21×** | +4.4 | 0.002 | 13/48 (HEC-1-A, LoVo, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +4.3 | 0.003 | 15/47 (HT-29, COLO 205, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 1.19× | +4.0 | 0.007 | 16/48 (HOP62, A498, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.28×** | +4.0 | 0.007 | 7/44 (NCI-H23, A-427, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.017 | 4/45 (MIA PaCa-2, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.025 | 12/46 (NCI-H23, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.029 | 9/45 (Hs 766T, SW 900, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.072 | 2/45 (CFPAC-1, HEC-1-A) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.21× | +3.1 | 0.10 | 5/46 (H4, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13264.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.451×** | -18.6 | 0e+00 | 37/46 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.476×** | -11.8 | 9e-30 | 32/45 (HEC-1-A, BT-474, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.512×** | -11.1 | 4e-26 | 30/44 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.600×** | -8.4 | 4e-15 | 26/47 (LoVo, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.690×** | -6.1 | 9e-08 | 24/46 (BT-474, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.783×** | -5.7 | 1e-06 | 22/45 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.733×** | -5.1 | 2e-05 | 15/46 (SNU-1, RKO, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.553×** | -5.1 | 2e-05 | 16/46 (SW48, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.758×** | -4.6 | 3e-04 | 15/46 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.761×** | -4.3 | 8e-04 | 18/45 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.761×** | -4.1 | 0.002 | 13/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.792×** | -3.7 | 0.010 | 18/45 (RKO, A-427, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.671×** | -3.4 | 0.025 | 9/23 (NCI-H1573, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.825×** | -3.2 | 0.058 | 14/46 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13264. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 33.8 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -25.0) |
| [[HEC-1-A (line)]] | alt | 28.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -15.0) |
| [[NCI-H460 (line)]] | wt | 14.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -16.0) |
| [[PANC-1 (line)]] | alt | 13.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -15.8) |
| [[SNU-1 (line)]] | wt | 35.6 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -17.3) |
| [[BT-474 (line)]] | alt | 18.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -14.7) |
| [[RKO (line)]] | wt | 15.8 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0746× (z -12.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -9.5) |
| [[SW480 (line)]] | alt | 13.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -15.4) |
| [[LoVo (line)]] | wt | 12.3 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.201× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 18.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -11.9) |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -11.5) |
| [[A-427 (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -11.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 8.83 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -9.2) |
| [[J82 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.292× (z -9.8) ⚠ cell-cycle shift, explains ~68% of this change |
| [[KATO III (line)]] | alt | 9.57 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 7.99 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 9.33 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.136× (z -10.0) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 17.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -12.5) |
| [[SW48 (line)]] | wt | 15.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0654× (z -10.4) |
| [[A-172 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13264), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GARNL3]] | +0.64 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[SLC29A2]] | +0.64 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[SFXN4]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.62 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[SORD]] | +0.62 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[ZP3]] | +0.61 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[UCK2]] | +0.60 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[ADAT2]] | +0.60 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[NAA25]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[ZNF891]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[ZNF692]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SLC19A1]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYNJ1]] | -0.57 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[SMIM14]] | -0.54 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[USP11]] | -0.54 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[FAM161B]] | -0.52 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[MED29]] | -0.51 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[ZNF490]] | -0.49 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM78B]] | B | FAM78B activity raises MCM3AP-AS1's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.38× lower at baseline in the lines without FAM78B | 0.057 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[TOP2A]] | B | TOP2A activity raises MCM3AP-AS1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DUXAP8]] | B | DUXAP8 activity raises MCM3AP-AS1's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.54× lower at baseline in the lines without DUXAP8 | 0.097 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.649). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-9.1, -38.2); signed map (-6.6, -54.2). **Vector** length 81.7, 15.4% of its response variance represented; |z| ≥ 3 in 916 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.4 | +6.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +4.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +3.6 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.9 | +3.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -11.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -18.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.4 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.3 | -11.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Methotrexate (drug)]] 0.5 µM |  | -1.1 | -0.9 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.1 | -0.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | MCM3AP antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 21q22.3 — chr21:46,229,196-46,259,390 (+) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ10508, NCRNA00031; previously C21orf85, MCM3APAS, MCM3AP-AS |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:16417](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16417) · Entrez [114044](https://www.ncbi.nlm.nih.gov/gene/114044) · Ensembl [ENSG00000215424](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215424)

## Data

Gene col 13264: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13264); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13264, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13264]; `tensor/DDL_lfc|DDL_z.npy` [13264]; `embed/gene_vectors.npy` [13264]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13264 or target_col == 13264). Every well: [[MCM3AP-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCM3AP-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
