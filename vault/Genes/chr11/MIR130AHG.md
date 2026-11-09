---
symbol: "MIR130AHG"
type: "gene"
col: 14883
ensembl_id: "ENSG00000254602"
name: "MIR130A host gene"
location: "11q12.1"
module: 10
arm: "+"
pooled_cpm: 3.27
n_lines_expressing: 36
n_dd_up: 1
n_dd_down: 9
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# MIR130AHG

*MIR130A host gene* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.71× (z +6.3, q 2e-07, up in 10 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.456× (z -6.2, q 4e-07, down in 11 of 17 measured lines) ⚠ toxic. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 5 µM: 0.529× (z -5.0, q 1e-04, down in 12 of 25 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLP1]] (+0.62, fdr 7e-06, ⚠ same locus), [[MIR1915HG]] (+0.56, fdr 2e-04), [[HSF2BP]] (+0.55, fdr 2e-05), [[LINC01776]] (+0.54, fdr 3e-05); moves opposite to [[SCARB1]] (-0.45, fdr 3e-04), [[SEC31A]] (-0.45, fdr 5e-04), [[TKT]] (-0.43, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC00466]] → it (grade B ⚠); 5 go from it, the strongest it → [[CLP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14883.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +6.3 | 2e-07 | 10/24 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14883.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.456×** | -6.2 | 4e-07 | 11/17 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.525×** | -5.3 | 4e-05 | 13/33 (HEC-1-A, A-427, …) | rises with dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.529×** | -5.0 | 1e-04 | 12/25 (A549, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.542×** | -4.8 | 2e-04 | 13/26 (HEC-1-A, A-427, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.597×** | -4.2 | 0.003 | 14/32 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.632×** | -3.7 | 0.016 | 13/30 (A-172, HEC-1-A, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.634×** | -3.7 | 0.016 | 11/31 (HEC-1-A, SNU-1, …) | two highest doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Gefitinib (drug)]] 5 µM |  | **0.676×** | -3.2 | 0.092 | 6/33 (PANC-1, A-427, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.635×** | -3.2 | 0.092 | 6/33 (LOX-IMVI, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.683× | -3.1 | 0.10 | 8/28 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.767× | -3.1 | 0.11 | 10/30 (SK-MEL-2, NCI-H460, …) | rises with dose | position effect removed |
| [[Fluvoxamine (maleate) (drug)]] 5 µM |  | 0.767× | -3.0 | 0.11 | 7/30 (SW 900, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14883. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.70 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0470× (z -11.4) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A-427 (line)]] | wt | 19.3 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0643× (z -14.3) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 11.5 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0441× (z -15.9) |
| [[MIA PaCa-2 (line)]] | alt | 5.27 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0990× (z -8.5) ⚠ toxic · without an alert: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.109× (z -8.5) |
| [[HOP62 (line)]] | alt | 4.93 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0891× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 5.60 | 0 | 1 | — | [[Larotrectinib (drug)]] 0.5 µM 0.0550× (z -9.8) |
| [[PANC-1 (line)]] | alt | 2.10 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0654× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[A498 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.988 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.242 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.56 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.218 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.276 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.230 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.261 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14883), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 12 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLP1]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[MIR1915HG]] | +0.56 | +0.57 / +0.32 | both halves | 2e-04 | same gene group |
| [[HSF2BP]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[LINC01776]] | +0.54 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[CCDC102A]] | +0.53 | +0.55 / +0.35 | both halves | 1e-04 |  |
| [[FRG1-DT]] | +0.50 | +0.51 / +0.32 | both halves | 2e-04 |  |
| [[PRKG1-AS1]] | +0.50 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[SNHG26]] | +0.47 | +0.48 / +0.37 | both halves | 9e-05 |  |
| [[ZNF594]] | +0.47 | +0.51 / +0.28 | both halves | 3e-04 |  |
| [[PIGV]] | +0.47 | +0.47 / +0.27 | both halves | 3e-04 |  |
| [[DDAH1]] | +0.46 | +0.47 / +0.38 | both halves | 6e-05 |  |
| [[ZNF793]] | +0.46 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[THBS4]] | +0.46 | +0.50 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCARB1]] | -0.45 | -0.46 / -0.29 | both halves | 3e-04 |  |
| [[SEC31A]] | -0.45 | -0.51 / -0.23 | both halves | 5e-04 |  |
| [[TKT]] | -0.43 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[KIF16B]] | -0.43 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[CLINT1]] | -0.41 | -0.42 / -0.25 | both halves | 4e-04 |  |
| [[PDXDC2P]] | -0.41 | -0.46 / -0.22 | both halves | 6e-04 |  |
| [[MLF1]] | -0.40 | -0.41 / -0.25 | both halves | 4e-04 |  |
| [[CBLB]] | -0.40 | -0.40 / -0.22 | both halves | 6e-04 |  |
| [[USP2]] | -0.40 | -0.26 / -0.33 | both halves | 4e-04 |  |
| [[ATP5F1C]] | -0.40 | -0.42 / -0.25 | both halves | 4e-04 |  |
| [[SUCO]] | -0.40 | -0.40 / -0.27 | both halves | 3e-04 |  |
| [[GFPT1]] | -0.40 | -0.41 / -0.21 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00466]] | B | LINC00466 activity raises MIR130AHG's level | lines that do not express LINC00466 (15) vs lines expressing it (35) | 2.40× lower at baseline in the lines without LINC00466 | 0.032 | ⚠ within organs, on part of the lines; also absent: FAM124A, NTN1, SSPOP; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLP1]] | B | MIR130AHG activity raises CLP1's level | lines that do not express MIR130AHG (14) vs lines expressing it (36) | 1.54× lower at baseline in the lines without MIR130AHG | 0.040 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: SPART, RAB34, PYGO1 |
| [[SNHG26]] | B | MIR130AHG activity raises SNHG26's level | lines that do not express MIR130AHG (14) vs lines expressing it (36) | 2.52× lower at baseline in the lines without MIR130AHG | 0.063 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: SPART, RAB34, PYGO1 |
| [[LINC00472]] | C | MIR130AHG activity raises LINC00472's level | lines that do not express MIR130AHG (14) vs lines expressing it (36) | 6.46× lower at baseline in the lines without MIR130AHG | 0.032 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: SPART, RAB34, PYGO1; co-absent with the target |
| [[FAT4]] | C | MIR130AHG activity raises FAT4's level | lines that do not express MIR130AHG (14) vs lines expressing it (36) | 6.81× lower at baseline in the lines without MIR130AHG | 0.084 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: SPART, RAB34, PYGO1; co-absent with the target |
| [[SYDE1]] | C | MIR130AHG activity raises SYDE1's level | lines that do not express MIR130AHG (14) vs lines expressing it (36) | 4.82× lower at baseline in the lines without MIR130AHG | 0.091 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: SPART, RAB34, PYGO1; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.331). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.8, 28.8); signed map (35.3, -10.9). **Vector** length 51.7, 9.37% of its response variance represented; |z| ≥ 3 in 667 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | +6.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.4 | +0.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +1.3 | +2.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +0.9 | +1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +0.9 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +0.8 | -0.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.8 | +2.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.7 | +0.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.7 | -6.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.1 | -4.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -1.7 | -5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.5 | -1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -1.5 | -3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.3 | -3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.2 | +0.1 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | MIR130A host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q12.1 — chr11:57,638,024-57,652,790 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55966](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55966) · Entrez [123466203](https://www.ncbi.nlm.nih.gov/gene/123466203) · Ensembl [ENSG00000254602](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254602)

## Data

Gene col 14883: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14883); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14883, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14883]; `tensor/DDL_lfc|DDL_z.npy` [14883]; `embed/gene_vectors.npy` [14883]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14883 or target_col == 14883). Every well: [[MIR130AHG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR130AHG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
