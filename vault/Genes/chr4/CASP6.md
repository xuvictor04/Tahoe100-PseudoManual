---
symbol: "CASP6"
type: "gene"
col: 6241
ensembl_id: "ENSG00000138794"
name: "caspase 6"
location: "4q25"
module: 72
arm: "+"
pooled_cpm: 10.74
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# CASP6

*caspase 6* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.26× (z +9.6, q 6e-19, up in 28 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.54× (z +7.1, q 2e-10, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.328× (z -13.1, q 3e-36, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMA1]] (+0.70, fdr 1e-05), [[GNPDA2]] (+0.67, fdr 2e-05), [[ITGAE]] (+0.65, fdr 1e-05); moves opposite to [[PFN1]] (-0.53, fdr 1e-04), [[SCART1]] (-0.51, fdr 3e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EPDR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6241.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +9.6 | 6e-19 | 28/36 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +8.5 | 7e-15 | 16/20 (LS 180, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +7.1 | 2e-10 | 29/48 (HS-578T, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +6.1 | 1e-07 | 22/40 (HEC-1-A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.67×** | +6.0 | 2e-07 | 29/47 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.67×** | +5.7 | 1e-06 | 23/46 (NCI-H460, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.58×** | +5.3 | 7e-06 | 25/47 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +4.5 | 5e-04 | 15/27 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +4.0 | 0.004 | 11/47 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.004 | 13/48 (AsPC-1, NCI-H1792, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.023 | 15/45 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.036 | 13/46 (J82, HOP62, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.042 | 10/47 (SW1417, SHP-77, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.046 | 8/45 (J82, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.058 | 10/48 (COLO 205, AsPC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.31×** | +3.1 | 0.058 | 11/48 (SW1417, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6241.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.328×** | -13.1 | 3e-36 | 44/48 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.349×** | -12.3 | 2e-32 | 36/46 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.554×** | -9.8 | 2e-20 | 28/45 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.437×** | -9.7 | 4e-20 | 38/46 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.450×** | -9.3 | 1e-18 | 37/46 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.386×** | -5.8 | 5e-07 | 29/47 (A-427, H4, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.635×** | -5.3 | 8e-06 | 23/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.638×** | -5.3 | 1e-05 | 21/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.685×** | -4.4 | 6e-04 | 21/44 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.522×** | -4.0 | 0.004 | 21/43 (HS-578T, SW48, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Hydroxyurea (drug)]] 5 µM |  | **0.721×** | -3.7 | 0.012 | 14/46 (HT-29, NCI-H2030, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.769× | -3.1 | 0.10 | 14/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6241. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.81 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -14.1) |
| [[LoVo (line)]] | wt | 12.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.227× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 6.27 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0352× (z -14.0) |
| [[A-172 (line)]] | wt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 5.45 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.100× (z -8.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 10.4 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0692× (z -8.7) |
| [[HOP62 (line)]] | alt | 5.81 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.133× (z -9.2) |
| [[J82 (line)]] | alt | 7.41 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -8.7) |
| [[KATO III (line)]] | alt | 12.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.164× (z -9.5) |
| [[LS 180 (line)]] | wt | 31.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.37× (z +11.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 5.83 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0321× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 9.09 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.101× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 8.23 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0838× (z -11.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 7.80 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -8.8) |
| [[RKO (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -9.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 7.92 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0776× (z -8.9) |
| [[SW48 (line)]] | wt | 18.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.107× (z -8.8) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW480 (line)]] | alt | 8.14 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.26× (z +9.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.92 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6241), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMA1]] | +0.70 | +0.77 / +0.53 | both halves | 1e-05 | pathway: Apoptosis |
| [[GNPDA2]] | +0.67 | +0.75 / +0.47 | both halves | 2e-05 |  |
| [[ITGAE]] | +0.65 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[EPDR1]] | +0.65 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[OSBPL1A]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[SPR]] | +0.65 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[PFDN4]] | +0.64 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[RTCA]] | +0.63 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[PSMC1]] | +0.62 | +0.67 / +0.46 | both halves | 3e-05 | pathway: Apoptosis |
| [[TXNL1]] | +0.62 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[ANKRD39]] | +0.61 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[RUFY2]] | +0.61 | +0.54 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PFN1]] | -0.53 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[SCART1]] | -0.51 | -0.50 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPDR1]] | B | EPDR1 activity lowers CASP6's level | lines that do not express EPDR1 (14) vs lines expressing it (36) | 1.33× higher at baseline in the lines without EPDR1 | 0.086 | ⚠ within organs, on part of the lines; also absent: RBM24, BEX2, GATA3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.615). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.1, -7.9); signed map (-26.6, -22.3). **Vector** length 69.1, 12.5% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antigen processing: Ub, ATP-independent proteasomal degradation* (reactome, mean cos +0.52 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +7.1 | +6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.5 | +5.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.4 | +5.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.9 | +7.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.4 | +0.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.6 | -9.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -12.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -9.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.2 | -13.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.3 | -9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.2 | +1.9 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -1.0 | -0.7 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.0 | -1.4 |
|  | [[Arbutin (drug)]] 0.05 µM |  | -0.9 | -0.4 |
|  | [[Tetracycline (hydrochloride) (drug)]] 5 µM |  | -0.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | caspase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:109,688,622-109,703,583 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MCH2, caspase-6, CSP-6 |
| Gene groups (HGNC) | Caspases |
| Hallmark sets | APOPTOSIS, XENOBIOTIC_METABOLISM, GLYCOLYSIS, HYPOXIA |
| Reactome | 9 pathways, smallest: Breakdown of the nuclear lamina; TP53 Regulates Transcription of Caspase Activators and Caspases; Caspase-mediated cleavage of cytoskeletal proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P55212](https://www.uniprot.org/uniprotkb/P55212) (Caspase-6):

> Cysteine protease that plays essential roles in programmed cell death, axonal degeneration, development and innate immunity. Acts as a non-canonical executioner caspase during apoptosis: localizes in the nucleus and cleaves the nuclear structural protein NUMA1 and lamin A/LMNA thereby inducing nuclear shrinkage and fragmentation. Lamin-A/LMNA cleavage is required for chromatin condensation and nuclear disassembly during apoptotic execution. Acts as a regulator of liver damage by promoting …

**Summary**, from NCBI Gene [839](https://www.ncbi.nlm.nih.gov/gene/839):

> This gene encodes a member of the cysteine-aspartic acid protease (caspase) family of enzymes. Sequential activation of caspases plays a central role in the execution-phase of cell apoptosis. Caspases exist as inactive proenzymes which undergo proteolytic processing at conserved aspartic acid residues to produce two subunits, large and small, that dimerize to form the active enzyme. This protein is processed by caspases 7, 8 and 10, and is thought to function as a downstream enzyme in the …

**Accessions** — [HGNC:1507](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1507) · Entrez [839](https://www.ncbi.nlm.nih.gov/gene/839) · UniProt [P55212](https://www.uniprot.org/uniprotkb/P55212) · Ensembl [ENSG00000138794](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138794)

## Data

Gene col 6241: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6241); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6241, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6241]; `tensor/DDL_lfc|DDL_z.npy` [6241]; `embed/gene_vectors.npy` [6241]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6241 or target_col == 6241). Every well: [[CASP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
