---
symbol: "LIF-AS2"
type: "gene"
col: 15607
ensembl_id: "ENSG00000268812"
name: "LIF antisense RNA 2"
location: "22q12.2"
module: 112
arm: "+"
pooled_cpm: 2.17
n_lines_expressing: 37
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# LIF-AS2

*LIF antisense RNA 2* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 3.28× (z +6.4, q 7e-08, up in 9 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.75× (z +4.3, q 0.002, up in 3 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.334× (z -5.9, q 2e-06, down in 24 of 32 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAF1]] (+0.62, fdr 1e-05), [[IL23A]] (+0.61, fdr 1e-05), [[CSF2]] (+0.60, fdr 1e-05); moves opposite to [[CCDC6]] (-0.48, fdr 7e-05), [[CPD]] (-0.47, fdr 2e-04), [[FAM120A]] (-0.47, fdr 2e-04).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LIF]] → it (grade B ⚠); 5 go from it, the strongest it → [[LINC00944]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 12 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15607.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.28×** | +6.4 | 7e-08 | 9/14 (NCI-H23, SNU-423, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.29×** | +6.2 | 2e-07 | 0/5 | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.27×** | +5.9 | 6e-07 | 1/5 (SW1417) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.08×** | +5.9 | 7e-07 | 4/9 (A498, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.93×** | +5.8 | 7e-07 | 0/7 | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **2.13×** | +5.8 | 7e-07 | 5/21 (A-172, SW1417, …) | inconsistent across doses | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +4.3 | 0.002 | 3/19 (LS 180, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.94×** | +3.6 | 0.020 | 8/33 (SNU-423, A498, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.94×** | +3.6 | 0.020 | 1/9 (SHP-77) | inconsistent across doses | low cells (technical?) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +3.6 | 0.020 | 4/15 (A-172, SW480, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.55×** | +3.4 | 0.041 | 6/30 (A498, H4, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.21×** | +3.3 | 0.045 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.1 | 0.072 | 3/21 (CFPAC-1, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.80×** | +3.1 | 0.073 | 10/25 (SNU-423, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15607.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.334×** | -5.9 | 2e-06 | 24/32 (SNU-423, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.344×** | -5.6 | 5e-06 | 22/31 (SNU-423, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.380×** | -5.2 | 3e-05 | 20/31 (SHP-77, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.479×** | -4.0 | 0.011 | 14/31 (SNU-423, NCI-H2347, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.490×** | -3.8 | 0.012 | 10/27 (SNU-423, AsPC-1, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.256×** | -3.8 | 0.012 | 12/29 (SNU-423, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.473×** | -3.7 | 0.016 | 12/31 (NCI-H23, HS-578T, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.523×** | -3.5 | 0.034 | 9/24 (NCI-H23, NCI-H2347, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.552×** | -3.2 | 0.078 | 12/31 (SNU-423, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 5 µM |  | **0.321×** | -3.2 | 0.078 | 4/28 (PANC-1, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[RMC-6236 (drug)]] 5 µM |  | **0.331×** | -3.1 | 0.095 | 1/29 (SHP-77) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.66 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15607. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 11.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -9.8) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0528× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 5.75 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0344× (z -10.9) |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0474× (z -11.0) |
| [[SW1417 (line)]] | alt | 8.16 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -9.6) |
| [[A-172 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.354 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.429 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.819 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.676 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.348 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.647 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.958 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.595 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.313 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.439 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.624 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.968 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.388 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.782 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.474 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.69 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15607), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAF1]] | +0.62 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[IL23A]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[CSF2]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[LIF]] | +0.60 | +0.58 / +0.59 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[CD70]] | +0.59 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[MIR3142HG]] | +0.59 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[LTB]] | +0.59 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[LHX1]] | +0.58 | +0.33 / +0.60 | both halves | 1e-04 |  |
| [[DYRK3]] | +0.57 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[NINJ1]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[NEURL3]] | +0.55 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[POMZP3]] | +0.53 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[IL1A]] | +0.53 | +0.50 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC6]] | -0.48 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[CPD]] | -0.47 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[FAM120A]] | -0.47 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[ADAM15]] | -0.46 | -0.29 / -0.47 | both halves | 3e-04 |  |
| [[DROSHA]] | -0.46 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[ELAC2]] | -0.46 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[MAP4]] | -0.45 | -0.31 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LIF]] | B | LIF activity raises LIF-AS2's level | lines that do not express LIF (10) vs lines expressing it (40) | 1.77× lower at baseline in the lines without LIF | 0.098 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: CD82, RABGEF1P3, ENSG00000236213 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00944]] | B | LIF-AS2 activity raises LINC00944's level | lines that do not express LIF-AS2 (13) vs lines expressing it (37) | 2.35× lower at baseline in the lines without LIF-AS2 | 0.069 | ⚠ within organs, on part of the lines; also absent: STING1, CFB; maybe low, not absent |
| [[CADM1]] | B | LIF-AS2 activity raises CADM1's level | lines that do not express LIF-AS2 (13) vs lines expressing it (37) | 2.14× lower at baseline in the lines without LIF-AS2 | 0.073 | ⚠ within organs, on part of the lines; also absent: STING1, CFB; maybe low, not absent |
| [[NFKBIE]] | B | LIF-AS2 activity raises NFKBIE's level | lines that do not express LIF-AS2 (13) vs lines expressing it (37) | 1.41× lower at baseline in the lines without LIF-AS2 | 0.074 | ⚠ within organs, on part of the lines; also absent: STING1, CFB; maybe low, not absent |
| [[TYMSOS]] | B | LIF-AS2 activity lowers TYMSOS's level | lines that do not express LIF-AS2 (13) vs lines expressing it (37) | 1.55× higher at baseline in the lines without LIF-AS2 | 0.081 | ⚠ within organs, on part of the lines; also absent: STING1, CFB; maybe low, not absent |
| [[CD82]] | B | LIF-AS2 activity raises CD82's level | lines that do not express LIF-AS2 (13) vs lines expressing it (37) | 2.76× lower at baseline in the lines without LIF-AS2 | 0.094 | ⚠ within organs, on part of the lines; also absent: STING1, CFB; maybe low, not absent |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.663). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.3, 1.6); signed map (42.1, 11.5). **Vector** length 50.5, 9.98% of its response variance represented; |z| ≥ 3 in 684 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.51 to 11); *KRAS signaling up* (hallmark, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.7 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | -2.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +2.0 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -3.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.9 | -4.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -1.7 | -2.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | LIF antisense RNA 2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 22q12.2 — chr22:30,246,205-30,246,998 (+) |
| Ensembl biotype | lncRNA |
| Also known as | TP53LC08 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28298](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28298) · Entrez [91370](https://www.ncbi.nlm.nih.gov/gene/91370) · Ensembl [ENSG00000268812](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000268812)

## Data

Gene col 15607: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15607); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15607, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15607]; `tensor/DDL_lfc|DDL_z.npy` [15607]; `embed/gene_vectors.npy` [15607]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15607 or target_col == 15607). Every well: [[LIF-AS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIF-AS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
