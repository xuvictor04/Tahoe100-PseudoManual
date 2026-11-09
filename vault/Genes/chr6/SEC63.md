---
symbol: "SEC63"
type: "gene"
col: 366
ensembl_id: "ENSG00000025796"
name: "SEC63 protein translocation regulator"
location: "6q21"
module: 42
arm: "+"
pooled_cpm: 201.43
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# SEC63

*SEC63 protein translocation regulator* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.31× (z +5.7, q 7e-06, up in 25 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.55× (z +4.9, q 2e-04, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.771× (z -7.4, q 7e-11, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GFPT1]] (+0.80, fdr 7e-06), [[SEC23A]] (+0.79, fdr 7e-06), [[TTC3]] (+0.79, fdr 7e-06); moves opposite to [[PNRC2]] (-0.70, fdr 7e-06), [[CARD6]] (-0.58, fdr 2e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 366.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +5.7 | 7e-06 | 25/44 (SNU-423, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.27×** | +5.2 | 6e-05 | 28/49 (SNU-423, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.55×** | +4.9 | 2e-04 | 32/48 (C32, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.8 | 0.021 | 21/48 (SW480, NCI-H2030, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.036 | 24/48 (NCI-H2030, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.061 | 25/49 (RKO, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.12× | +3.1 | 0.18 | 8/48 (SW480, SNU-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 366.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.771×** | -7.4 | 7e-11 | 37/48 (A498, HS-578T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.703×** | -7.3 | 7e-11 | 38/47 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.744×** | -6.1 | 2e-07 | 31/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.799×** | -6.0 | 4e-07 | 30/49 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.805×** | -5.8 | 7e-07 | 24/48 (NCI-H1573, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.769×** | -5.7 | 1e-06 | 31/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.792×** | -5.0 | 4e-05 | 36/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.795×** | -5.0 | 5e-05 | 29/48 (A-172, A498, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.792×** | -4.8 | 8e-05 | 28/48 (A498, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.800×** | -4.8 | 9e-05 | 27/48 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.816×** | -4.1 | 0.002 | 25/47 (SNU-1, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -3.9 | 0.005 | 22/48 (A-172, HS-578T, …) | inconsistent across doses | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.836× | -3.7 | 0.009 | 22/50 (AN3 CA, SW 900, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.958× | -3.3 | 0.036 | 0/50 | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.859× | -3.3 | 0.039 | 12/49 (HT-29, HEC-1-A, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.862× | -3.2 | 0.047 | 15/48 (LOX-IMVI, KATO III, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.862× | -3.2 | 0.047 | 20/48 (NCI-H661, BT-474, …) | two highest doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.865× | -3.1 | 0.057 | 12/49 (HEC-1-A, HT-29, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.866× | -3.1 | 0.057 | 13/48 (LoVo, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 366. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 184 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -17.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.426× (z -13.4) |
| [[A498 (line)]] | wt | 201 | 0 | 4 | — | [[Harringtonine (drug)]] 0.5 µM 0.455× (z -12.9) |
| [[A-427 (line)]] | wt | 167 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.78× (z +10.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 217 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.493× (z -9.7) |
| [[HS-578T (line)]] | alt | 287 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.645× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 252 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -8.9) |
| [[J82 (line)]] | alt | 207 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 124 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 1.94× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Selinexor (drug)]] 5 µM 0.562× (z -9.4) |
| [[SNU-423 (line)]] | alt | 263 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +11.2) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 195 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.569× (z -8.8) |
| [[BT-474 (line)]] | alt | 161 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.555× (z -8.9) |
| [[KATO III (line)]] | alt | 262 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.467× (z -9.7) ⚠ toxic |
| [[LoVo (line)]] | wt | 225 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 229 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -9.3) |
| [[NCI-H661 (line)]] | alt | 287 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.306× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 171 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +10.7) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 181 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.38× (z +9.6) | — |
| [[A549 (line)]] | wt | 153 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 310 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 256 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 98.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 232 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 192 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 205 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 160 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 192 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 181 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 192 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 165 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 370 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 142 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 260 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 198 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 366), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GFPT1]] | +0.80 | +0.82 / +0.74 | both halves | 7e-06 |  |
| [[SEC23A]] | +0.79 | +0.77 / +0.71 | both halves | 7e-06 | STRING 457 |
| [[TTC3]] | +0.79 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[EPRS1]] | +0.78 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[NUCB2]] | +0.72 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.72 | +0.82 / +0.60 | both halves | 7e-06 |  |
| [[DNAJC3]] | +0.72 | +0.76 / +0.71 | both halves | 7e-06 | same gene group; STRING 750 |
| [[SSR1]] | +0.72 | +0.64 / +0.71 | both halves | 7e-06 | STRING 708 |
| [[SSR3]] | +0.71 | +0.66 / +0.65 | both halves | 7e-06 | STRING 533 |
| [[OSTC]] | +0.71 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[SEL1L]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 | STRING 521 |
| [[GORASP2]] | +0.70 | +0.79 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNRC2]] | -0.70 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[CARD6]] | -0.58 | -0.47 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SEC63's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HOOK1]] | B | HOOK1 activity lowers SEC63's level | lines that do not express HOOK1 (22) vs lines expressing it (28) | 1.27× higher at baseline in the lines without HOOK1 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SMPDL3B, BSPRY, SPINT1-AS1 |
| [[TOP2B]] | B | TOP2B activity raises SEC63's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.761). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.0, -32.8); signed map (-52.7, 9.7). **Vector** length 146, 48.8% of its response variance represented; |z| ≥ 3 in 930 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.64 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.59 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.59 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +5.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.5 | +0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.3 | +0.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.8 | +3.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.7 | +1.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +2.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.6 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -8.2 | -7.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.8 | -6.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.8 | -5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.7 | -7.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.6 | -5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.6 | -4.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.3 | -3.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | SEC63 protein translocation regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:107,867,756-107,958,208 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SEC63L, PRO2507, ERdj2, DNAJC23 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UGP8](https://www.uniprot.org/uniprotkb/Q9UGP8) (Translocation protein SEC63 homolog):

> Mediates cotranslational and post-translational transport of certain precursor polypeptides across endoplasmic reticulum (ER). Proposed to play an auxiliary role in recognition of precursors with short and apolar signal peptides. May cooperate with SEC62 and HSPA5/BiP to facilitate targeting of small presecretory proteins into the SEC61 channel-forming translocon complex, triggering channel opening for polypeptide translocation to the ER lumen. Required for efficient PKD1/Polycystin-1 …

**Summary**, from NCBI Gene [11231](https://www.ncbi.nlm.nih.gov/gene/11231):

> The Sec61 complex is the central component of the protein translocation apparatus of the endoplasmic reticulum (ER) membrane. The protein encoded by this gene and SEC62 protein are found to be associated with ribosome-free SEC61 complex. It is speculated that Sec61-Sec62-Sec63 may perform post-translational protein translocation into the ER. The Sec61-Sec62-Sec63 complex might also perform the backward transport of ER proteins that are subject to the ubiquitin-proteasome-dependent degradation …

**Accessions** — [HGNC:21082](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21082) · Entrez [11231](https://www.ncbi.nlm.nih.gov/gene/11231) · UniProt [Q9UGP8](https://www.uniprot.org/uniprotkb/Q9UGP8) · Ensembl [ENSG00000025796](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000025796)

## Data

Gene col 366: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 366); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 366, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 366]; `tensor/DDL_lfc|DDL_z.npy` [366]; `embed/gene_vectors.npy` [366]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 366 or target_col == 366). Every well: [[SEC63 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC63.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
