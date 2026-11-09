---
symbol: "CENPQ"
type: "gene"
col: 401
ensembl_id: "ENSG00000031691"
name: "centromere protein Q"
location: "6p12.3"
module: 6
arm: "+"
pooled_cpm: 23.2
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CENPQ

*centromere protein Q* — 6p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.69× (z +9.2, q 3e-17, up in 28 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 5 µM: 2.14× (z +6.2, q 4e-08, up in 22 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.583× (z -9.4, q 2e-18, down in 38 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.804× (z -5.4, q 1e-05, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZGRF1]] (+0.80, fdr 7e-06), [[MTBP]] (+0.78, fdr 7e-06), [[RAD51AP1]] (+0.75, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF257]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 401.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **1.69×** | +9.2 | 3e-17 | 28/43 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.57×** | +7.8 | 1e-12 | 31/48 (NCI-H460, A498, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.66×** | +7.6 | 4e-12 | 27/44 (J82, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.53×** | +7.4 | 1e-11 | 30/47 (LoVo, A549, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **1.57×** | +6.8 | 1e-09 | 22/36 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.47×** | +6.8 | 1e-09 | 33/48 (LoVo, A549, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.55×** | +6.6 | 3e-09 | 25/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.14×** | +6.2 | 4e-08 | 22/47 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.48×** | +5.9 | 3e-07 | 28/48 (SW480, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.26×** | +5.7 | 9e-07 | 20/47 (J82, SW480, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.99×** | +5.6 | 1e-06 | 23/46 (RKO, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | **1.35×** | +4.8 | 7e-05 | 19/39 (SW1417, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.20×** | +4.6 | 2e-04 | 11/48 (SK-MEL-2, HS-578T, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.34×** | +4.4 | 5e-04 | 18/47 (SNU-423, KATO III, …) | all doses, stronger at high dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.19× | +4.3 | 7e-04 | 18/48 (NCI-H23, A-427, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.8 | 0.005 | 20/48 (J82, SW1417, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.034 | 7/48 (PANC-1, AsPC-1, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.20× | +3.1 | 0.050 | 11/47 (SHP-77, KATO III, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.050 | 7/48 (SW480, COLO 205, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.065 | 11/48 (LOX-IMVI, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 401.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.583×** | -9.4 | 2e-18 | 38/48 (Hs 766T, HT-29, …) | all doses, flat |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.624×** | -5.7 | 4e-06 | 25/48 (SW480, A498, …) | two highest doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.804×** | -5.4 | 1e-05 | 23/47 (HEC-1-A, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.587×** | -4.3 | 0.002 | 20/46 (HCT15, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.619×** | -3.9 | 0.011 | 14/48 (SHP-77, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.776×** | -3.8 | 0.012 | 12/47 (HEC-1-A, A-427, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.860× | -3.7 | 0.015 | 12/48 (RKO, AsPC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.822×** | -3.4 | 0.042 | 16/47 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | 0.682× | -3.1 | 0.12 | 12/47 (HEC-1-A, KATO III, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 401. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 41.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -12.0) |
| [[SW480 (line)]] | alt | 35.5 | 2 (2 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +9.1) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[A-427 (line)]] | wt | 25.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.332× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -10.6) |
| [[H4 (line)]] | wt | 24.7 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0643× (z -12.7) |
| [[Hs 766T (line)]] | wt | 18.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.219× (z -9.1) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 21.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -10.0) |
| [[SW48 (line)]] | wt | 17.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.137× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 401), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZGRF1]] | +0.80 | +0.81 / +0.77 | both halves | 7e-06 |  |
| [[MTBP]] | +0.78 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[RAD51AP1]] | +0.75 | +0.74 / +0.74 | both halves | 7e-06 | STRING 472 |
| [[CENPU]] | +0.74 | +0.71 / +0.74 | both halves | 7e-06 | same gene group; pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 999 |
| [[ATAD5]] | +0.73 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[FANCI]] | +0.73 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[SPC25]] | +0.72 | +0.70 / +0.71 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 429 |
| [[RFC3]] | +0.71 | +0.76 / +0.66 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[CENPK]] | +0.71 | +0.71 / +0.68 | both halves | 7e-06 | same gene group; pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 999 |
| [[CHAF1A]] | +0.71 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[BRCA1]] | +0.71 | +0.65 / +0.74 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[PSMC3IP]] | +0.70 | +0.62 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF257]] | B | ZNF257 activity raises CENPQ's level | lines that do not express ZNF257 (35) vs lines expressing it (15) | 1.31× lower at baseline in the lines without ZNF257 | 0.062 | ⚠ within organs, on part of the lines; also absent: ZNF208, LINC01615, ZNF732 |
| [[TOP2A]] | B | TOP2A activity lowers CENPQ's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.641). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.5, -48.1); signed map (-40.7, -42.5). **Vector** length 104, 25.4% of its response variance represented; |z| ≥ 3 in 861 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.53 to 28); *DNA Replication* (reactome, mean cos +0.52 to 40); *E2F G1/S* (control, mean cos +0.50 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +3.5 | +5.9 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +3.4 | +4.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +3.4 | +6.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.2 | +6.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.3 | +1.4 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.1 | +1.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.8 | -9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | -5.4 |
|  | [[EX229 (drug)]] 5 µM |  | -4.2 | -3.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.2 | -4.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.9 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.7 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | centromere protein Q |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.3 — chr6:49,463,370-49,493,107 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10545, CENP-Q; previously C6orf139 |
| Gene groups (HGNC) | Constitutive centromere associated network |
| Reactome | 20 pathways, smallest: Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L2Z9](https://www.uniprot.org/uniprotkb/Q7L2Z9) (Centromere protein Q):

> Component of the CENPA-CAD (nucleosome distal) complex, a complex recruited to centromeres which is involved in assembly of kinetochore proteins, mitotic progression and chromosome segregation. May be involved in incorporation of newly synthesized CENPA into centromeres via its interaction with the CENPA-NAC complex. Plays an important role in chromosome congression and in the recruitment of CENP-O complex (which comprises CENPO, CENPP, CENPQ and CENPU), CENPE and PLK1 to the kinetochores.

**Summary**, from NCBI Gene [55166](https://www.ncbi.nlm.nih.gov/gene/55166):

> CENPQ is a subunit of a CENPH (MIM 605607)-CENPI (MIM 300065)-associated centromeric complex that targets CENPA (MIM 117139) to centromeres and is required for proper kinetochore function and mitotic progression (Okada et al., 2006 [PubMed 16622420]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:21347](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21347) · Entrez [55166](https://www.ncbi.nlm.nih.gov/gene/55166) · UniProt [Q7L2Z9](https://www.uniprot.org/uniprotkb/Q7L2Z9) · Ensembl [ENSG00000031691](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000031691)

## Data

Gene col 401: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 401); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 401, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 401]; `tensor/DDL_lfc|DDL_z.npy` [401]; `embed/gene_vectors.npy` [401]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 401 or target_col == 401). Every well: [[CENPQ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CENPQ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
