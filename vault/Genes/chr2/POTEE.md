---
symbol: "POTEE"
type: "gene"
col: 11989
ensembl_id: "ENSG00000188219"
name: "POTE ankyrin domain family member E"
location: "2q21.1"
module: 96
arm: "+"
pooled_cpm: 2.16
n_lines_expressing: 21
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# POTEE

*POTE ankyrin domain family member E* — 2q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.84× (z +11.9, q 4e-30, up in 10 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POTEF]] (+0.73, fdr 7e-06), [[FAR2P1]] (+0.54, fdr 1e-04), [[MBD6]] (+0.50, fdr 8e-05); moves opposite to [[TMTC2]] (-0.45, fdr 1e-04), [[ABHD17B]] (-0.45, fdr 2e-04), [[VDAC1]] (-0.43, fdr 2e-04).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FAR2P1]], [[POTEF]] → it (grade C ⚠); 5 go from it, the strongest it → [[PANK4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11989.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.84×** | +11.9 | 4e-30 | 10/13 (SNU-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.76×** | +9.8 | 3e-20 | 3/6 (HEC-1-A, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.02×** | +8.4 | 8e-15 | 2/2 (HEC-1-A, BT-474) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.13×** | +7.6 | 4e-12 | 3/3 (HEC-1-A, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **3.12×** | +7.2 | 1e-10 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.04×** | +7.0 | 3e-10 | 15/16 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.75×** | +6.3 | 2e-08 | 14/16 (SNU-423, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.04×** | +5.8 | 4e-07 | 9/12 (C-33 A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.27×** | +5.1 | 2e-05 | 5/9 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.00×** | +4.9 | 5e-05 | 1/6 (NCI-H23) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **2.12×** | +4.7 | 1e-04 | 10/16 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +4.6 | 2e-04 | 0/14 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **2.29×** | +4.3 | 7e-04 | 1/9 (PANC-1) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.59×** | +4.3 | 9e-04 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.53×** | +4.2 | 0.001 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | **1.74×** | +3.5 | 0.014 | 0/10 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.74×** | +3.5 | 0.014 | 0/9 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.015 | 0/17 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.89×** | +3.4 | 0.016 | 0/8 | inconsistent across doses | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.017 | 0/15 | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +3.1 | 0.037 | 6/15 (SNU-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11989.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.569× | -3.6 | 0.19 | 8/18 (A-427, NCI-H1573, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.613× | -3.1 | 0.41 | 7/16 (HepG2/C3A, A-427, …) | rises with dose | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.621× | -3.0 | 0.41 | 10/18 (KATO III, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11989. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.88× (z +9.3) | — |
| [[SNU-1 (line)]] | wt | 17.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +10.0) | — |
| [[A-172 (line)]] | wt | 0.230 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.616 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.182 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.203 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.205 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.224 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.319 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.228 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.268 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.211 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.316 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.190 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.286 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.767 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.184 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.172 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.190 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.195 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.229 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.188 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.810 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.242 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.205 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.214 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.654 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.360 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.578 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.635 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11989), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POTEF]] | +0.73 | +0.75 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[FAR2P1]] | +0.54 | +0.36 / +0.63 | both halves | 1e-04 |  |
| [[MBD6]] | +0.50 | +0.37 / +0.60 | both halves | 8e-05 |  |
| [[IL11RA]] | +0.45 | +0.45 / +0.37 | both halves | 8e-05 |  |
| [[AAAS]] | +0.45 | +0.37 / +0.44 | both halves | 8e-05 |  |
| [[ABHD16A]] | +0.45 | +0.36 / +0.36 | both halves | 1e-04 |  |
| [[TFE3]] | +0.45 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[RHOT2]] | +0.44 | +0.40 / +0.39 | both halves | 6e-05 |  |
| [[FSTL4]] | +0.44 | +0.55 / +0.18 | ⚠ one half (not replicated) | 9e-04 |  |
| [[C1orf226]] | +0.44 | +0.40 / +0.26 | both halves | 4e-04 |  |
| [[RNF40]] | +0.43 | +0.37 / +0.36 | both halves | 1e-04 |  |
| [[SF3A1]] | +0.43 | +0.26 / +0.49 | both halves | 3e-04 |  |
| [[CCDC113]] | +0.43 | +0.31 / +0.41 | both halves | 2e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMTC2]] | -0.45 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[ABHD17B]] | -0.45 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[VDAC1]] | -0.43 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[SOS1]] | -0.42 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[TPI1]] | -0.42 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[TNFRSF10A]] | -0.40 | -0.29 / -0.43 | both halves | 3e-04 |  |
| [[FBXW11]] | -0.38 | -0.29 / -0.35 | both halves | 2e-04 |  |
| [[TXN]] | -0.38 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[SLC16A1]] | -0.38 | -0.30 / -0.27 | both halves | 3e-04 |  |
| [[PRDX1]] | -0.38 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[CGAS]] | -0.37 | -0.32 / -0.27 | both halves | 3e-04 |  |
| [[MCM9]] | -0.37 | -0.37 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAR2P1]], [[POTEF]] | C | FAR2P1, POTEF activity raises POTEE's level | lines that do not express FAR2P1, POTEF (29) vs lines expressing them (21) | 3.25× lower at baseline in the lines without FAR2P1, POTEF | 0.001 | ⚠ within organs, on part of the lines; also absent: POTEE, ENSG00000264660, ENSG00000286329; co-absent with the target; co-absent genes |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PANK4]] | B | POTEE activity raises PANK4's level | lines that do not express POTEE (29) vs lines expressing it (21) | 1.29× lower at baseline in the lines without POTEE | 0.054 | ⚠ within organs, on part of the lines; also absent: FAR2P1, ENSG00000286329, EPIC1 |
| [[RPS6KB2]] | B | POTEE activity strengthens RPS6KB2's drug response | lines that do not express POTEE (29) vs lines expressing it (19) | the lines without POTEE respond 0.80× as strongly (z diff +0.97); strongest at Dinaciclib 5 µM: 1.60x vs 2.81x (z diff +3.2) | 0.069 | ⚠ within organs, on part of the lines; also absent: FAR2P1, ENSG00000286329, EPIC1; target measured in part of the lines; artifact flags |
| [[TNKS1BP1]] | B | POTEE activity lowers TNKS1BP1's level | lines that do not express POTEE (29) vs lines expressing it (21) | 1.43× higher at baseline in the lines without POTEE | 0.098 | ⚠ within organs, on part of the lines; also absent: FAR2P1, ENSG00000286329, EPIC1 |
| [[FAR2P1]] | C | POTEE activity raises FAR2P1's level | lines that do not express POTEE (29) vs lines expressing it (21) | 8.70× lower at baseline in the lines without POTEE | 4e-06 | ⚠ within organs, on part of the lines; also absent: FAR2P1, ENSG00000286329, EPIC1; co-absent with the target |
| [[POTEF]] | C | POTEE activity raises POTEF's level | lines that do not express POTEE (29) vs lines expressing it (21) | 10.32× lower at baseline in the lines without POTEE | 9e-06 | ⚠ within organs, on part of the lines; also absent: FAR2P1, ENSG00000286329, EPIC1; co-absent with the target |

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.484). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-32.7, 27.6); signed map (0.2, -7.2). **Vector** length 23.3, 3.73% of its response variance represented; |z| ≥ 3 in 362 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +7.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.5 | +7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.1 | +11.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.8 | +2.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.6 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.6 | +1.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | +2.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | -0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.6 | -0.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.6 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.6 | -0.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -1.1 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | POTE ankyrin domain family member E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.1 — chr2:131,209,536-131,265,278 (+) |
| Ensembl biotype | protein_coding |
| Also known as | POTE2, POTE-2, A26C1, POTE2gamma, CT104.2; previously A26C1A |
| Gene groups (HGNC) | POTE ankyrin domain containing |
| Reactome | 4 pathways, smallest: RHOF GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

UniProt [Q6S8J3](https://www.uniprot.org/uniprotkb/Q6S8J3) carries no function annotation.

**Summary**, from NCBI Gene [445582](https://www.ncbi.nlm.nih.gov/gene/445582):

> Predicted to enable protein kinase binding activity. Predicted to be a structural constituent of postsynaptic actin cytoskeleton. Involved in substantia nigra development. Located in blood microparticle; extracellular exosome; and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:33895](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33895) · Entrez [445582](https://www.ncbi.nlm.nih.gov/gene/445582) · UniProt [Q6S8J3](https://www.uniprot.org/uniprotkb/Q6S8J3) · Ensembl [ENSG00000188219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188219)

## Data

Gene col 11989: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11989); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11989, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11989]; `tensor/DDL_lfc|DDL_z.npy` [11989]; `embed/gene_vectors.npy` [11989]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11989 or target_col == 11989). Every well: [[POTEE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POTEE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
