---
symbol: "POLR3H"
type: "gene"
col: 1954
ensembl_id: "ENSG00000100413"
name: "RNA polymerase III subunit H"
location: "22q13.2"
module: 33
arm: "+"
pooled_cpm: 8.35
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# POLR3H

*RNA polymerase III subunit H* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.05× (z +10.4, q 2e-22, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.652× (z -8.7, q 1e-15, down in 24 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR1B]] (+0.76, fdr 7e-06), [[MYBBP1A]] (+0.76, fdr 7e-06), [[TMEM201]] (+0.72, fdr 7e-06); moves opposite to [[ZC3H6]] (-0.63, fdr 1e-05), [[CYLD]] (-0.62, fdr 7e-06), [[SMIM14]] (-0.61, fdr 7e-06).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FAM78B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1954.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.05×** | +10.4 | 2e-22 | 35/47 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.67×** | +7.4 | 3e-11 | 27/46 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +5.0 | 1e-04 | 13/47 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +4.6 | 6e-04 | 16/45 (NCI-H460, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.38×** | +4.5 | 6e-04 | 12/39 (KATO III, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.32×** | +4.1 | 0.004 | 15/47 (A549, NCI-H1573, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.006 | 9/45 (HS-578T, LOX-IMVI, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.23× | +3.0 | 0.16 | 5/46 (SW480, SNU-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1954.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.652×** | -8.7 | 1e-15 | 24/45 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.548×** | -8.7 | 1e-15 | 29/47 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.555×** | -8.5 | 4e-15 | 27/46 (NCI-H2030, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.546×** | -8.4 | 7e-15 | 26/45 (SW48, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.643×** | -6.4 | 2e-08 | 20/46 (BT-474, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.655×** | -5.8 | 5e-07 | 21/45 (A-172, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.661×** | -5.7 | 8e-07 | 21/45 (SW48, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.706×** | -5.0 | 4e-05 | 18/46 (C-33 A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.712×** | -4.7 | 2e-04 | 18/46 (SW48, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.730×** | -4.5 | 3e-04 | 16/46 (A-427, CHP-212, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.832×** | -3.7 | 0.010 | 14/44 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 0.5 µM |  | **0.783×** | -3.5 | 0.021 | 11/45 (RKO, SK-MEL-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.790×** | -3.4 | 0.032 | 18/42 (RKO, PANC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1954. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 10.1 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.105× (z -9.1) |
| [[LoVo (line)]] | wt | 10.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.244× (z -8.6) |
| [[PANC-1 (line)]] | alt | 8.73 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.233× (z -10.2) |
| [[SNU-1 (line)]] | wt | 22.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -8.7) |
| [[SW48 (line)]] | wt | 19.5 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -9.9) |
| [[A-427 (line)]] | wt | 8.81 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -8.6) |
| [[A498 (line)]] | wt | 7.95 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.337× (z -9.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[C-33 A (line)]] | alt | 15.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 8.85 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -8.7) |
| [[KATO III (line)]] | alt | 9.95 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 8.71 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0660× (z -14.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -8.8) |
| [[RKO (line)]] | wt | 13.6 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0864× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 33.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -10.5) |
| [[SNU-423 (line)]] | alt | 5.85 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0994× (z -9.4) |
| [[A-172 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1954), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR1B]] | +0.76 | +0.72 / +0.75 | both halves | 7e-06 | same gene group; STRING 906 |
| [[MYBBP1A]] | +0.76 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[TMEM201]] | +0.72 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[NOL10]] | +0.71 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[DCAF1]] | +0.71 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.71 | +0.68 / +0.75 | both halves | 7e-06 | same gene group; STRING 936 |
| [[POLR3B]] | +0.71 | +0.66 / +0.66 | both halves | 7e-06 | same gene group; pathway: Cytosolic sensors of pathogen-associated DNA; STRING 999 |
| [[CHCHD6]] | +0.71 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[TBRG4]] | +0.70 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[MRPL4]] | +0.70 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[RRP7BP]] | +0.70 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[NLE1]] | +0.70 | +0.64 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H6]] | -0.63 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[CYLD]] | -0.62 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[SMIM14]] | -0.61 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[ABCA5]] | -0.61 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[CERT1]] | -0.60 | -0.54 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM78B]] | B | FAM78B activity raises POLR3H's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.41× lower at baseline in the lines without FAM78B | 0.053 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[TOP2A]] | B | TOP2A activity raises POLR3H's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers POLR3H's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.787). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.8, -39.6); signed map (-10.6, -51.3). **Vector** length 76.3, 13.0% of its response variance represented; |z| ≥ 3 in 971 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.54 to 8); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.54 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.54 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +5.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.1 | +10.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +1.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.9 | +4.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +4.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.9 | +2.5 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -8.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -3.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.7 | -5.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -0.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase III subunit H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:41,525,799-41,544,606 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RPC8, KIAA1665, C25 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Reactome | 10 pathways, smallest: RNA Polymerase III Chain Elongation; RNA Polymerase III Transcription Termination; RNA Polymerase III Transcription Initiation From Type 2 Promoter |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y535](https://www.uniprot.org/uniprotkb/Q9Y535) (DNA-directed RNA polymerase III subunit RPC8):

> DNA-dependent RNA polymerase catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates. Specific peripheric component of RNA polymerase III (Pol III) which synthesizes small non-coding RNAs including 5S rRNA, snRNAs, tRNAs and miRNAs from at least 500 distinct genomic loci. With CRCP/RPC9 forms a mobile stalk that protrudes from Pol III core and functions primarily in transcription initiation (By similarity). Pol III plays a key role in sensing and …

**Summary**, from NCBI Gene [171568](https://www.ncbi.nlm.nih.gov/gene/171568):

> Enables DNA-directed RNA polymerase activity. Involved in termination of RNA polymerase III transcription and transcription initiation at RNA polymerase III promoter. Located in centrosome and nucleoplasm. Part of RNA polymerase III complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30349](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30349) · Entrez [171568](https://www.ncbi.nlm.nih.gov/gene/171568) · UniProt [Q9Y535](https://www.uniprot.org/uniprotkb/Q9Y535) · Ensembl [ENSG00000100413](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100413)

## Data

Gene col 1954: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1954); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1954, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1954]; `tensor/DDL_lfc|DDL_z.npy` [1954]; `embed/gene_vectors.npy` [1954]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1954 or target_col == 1954). Every well: [[POLR3H — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR3H.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
