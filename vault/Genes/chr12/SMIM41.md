---
symbol: "SMIM41"
type: "gene"
col: 16073
ensembl_id: "ENSG00000284791"
name: "small integral membrane protein 41"
location: "12q13.13"
module: 47
arm: "+"
pooled_cpm: 4.55
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 21
n_dd_up_clean: 13
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/047", "written"]
generated_by: "tahoemap"
---

# SMIM41

*small integral membrane protein 41* — 12q13.13

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> SMIM41 encodes a 93-residue predicted single-pass membrane protein, and nothing about its function is established.

## What it is

What exists is annotation. The gene sits on chromosome 12q13.13, has three small exons, and predicts a protein of about 9 kDa with one transmembrane helix near the middle of the sequence. "Membrane" is its only cellular-component term, assigned by automated inference rather than experiment. There is no identified binding partner, no reported knockout phenotype, no pathway membership, and the mouse orthologue is equally uncharacterised. The SMIM prefix is a naming convention for short predicted membrane proteins, not a family with shared biology, so the other SMIM genes say nothing about this one.

## What is uncertain

Everything past its coordinates. The transcript is low in every line, and at low counts a co-expression rank is as compatible with shared depth and ambient-RNA structure as with real covariation. With no known function there is nothing to predict and no mechanism against which the correlation could be judged; whether the open reading frame is appreciably translated has not been shown.

## References

No primary literature I can cite with confidence.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.65× (z +12.2, q 3e-31, up in 27 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.324× (z -7.5, q 4e-11, down in 28 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PYGM]] (+0.82, fdr 7e-06), [[TINCR]] (+0.82, fdr 7e-06), [[RFPL3S]] (+0.82, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[FAM83E]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16073.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.65×** | +12.2 | 3e-31 | 27/36 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.20×** | +10.9 | 3e-25 | 30/37 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.91×** | +7.1 | 3e-10 | 28/41 (HOP62, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.37×** | +5.7 | 1e-06 | 23/45 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.20×** | +5.2 | 2e-05 | 20/44 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Vilanterol (drug)]] 5 µM |  | **1.54×** | +4.0 | 0.005 | 13/43 (Panc 03.27, NCI-H2030, …) | rises with dose | position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.007 | 15/45 (SHP-77, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.79×** | +3.9 | 0.008 | 13/46 (SW480, A498, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.75×** | +3.7 | 0.014 | 9/37 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +3.5 | 0.029 | 17/42 (A549, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.71×** | +3.4 | 0.032 | 1/5 (NCI-H2347) | all doses, flat | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +3.4 | 0.032 | 13/47 (A-427, NCI-H2347, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.48×** | +3.2 | 0.069 | 7/41 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Naproxen (drug)]] 0.05 µM |  | **1.67×** | +3.1 | 0.071 | 11/35 (LOX-IMVI, AsPC-1, …) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.072 | 6/44 (H4, C-33 A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16073.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.324×** | -7.5 | 4e-11 | 28/42 (NCI-H1573, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.376×** | -6.5 | 2e-08 | 25/46 (A-427, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.397×** | -6.1 | 2e-07 | 26/43 (AsPC-1, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.420×** | -5.8 | 1e-06 | 25/41 (H4, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.427×** | -5.4 | 6e-06 | 24/40 (A-427, LoVo, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.442×** | -5.0 | 5e-05 | 27/44 (NCI-H23, H4, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.591×** | -4.9 | 1e-04 | 25/44 (NCI-H23, A-427, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.476×** | -4.7 | 2e-04 | 21/40 (SW 900, NCI-H23, …) | all doses, flat |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.478×** | -4.7 | 2e-04 | 26/37 (AsPC-1, H4, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **0.483×** | -4.7 | 2e-04 | 22/45 (AsPC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.507×** | -4.5 | 3e-04 | 19/32 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.518×** | -4.4 | 6e-04 | 18/44 (SK-MEL-2, NCI-H23, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.527×** | -4.3 | 9e-04 | 18/43 (H4, SW1417, …) | top dose only |  |
| [[Erlotinib (drug)]] 5 µM |  | **0.561×** | -3.7 | 0.009 | 16/39 (NCI-H2030, BT-474, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.582×** | -3.5 | 0.020 | 17/38 (PANC-1, SW480, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.671×** | -3.3 | 0.034 | 12/42 (AsPC-1, SW1417, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16073. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 13.0 | 0 | 5 | — | [[Digitoxin (drug)]] 0.5 µM 0.0307× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 9.12 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0355× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 14.4 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 9.70× (z +11.2) | [[Harringtonine (drug)]] 5 µM 0.0696× (z -8.8) |
| [[A-427 (line)]] | wt | 10.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.00978× (z -16.3) |
| [[A498 (line)]] | wt | 5.08 | 0 | 2 | — | [[Harringtonine (drug)]] 0.05 µM 0.0564× (z -8.9) |
| [[LoVo (line)]] | wt | 7.39 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +11.7) | [[Belumosudil (drug)]] 5 µM 0.0649× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0214× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 2.15 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 39.4× (z +14.5) | — |
| [[C32 (line)]] | wt | 3.56 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 129× (z +13.5) | — |
| [[hTERT-HPNE (line)]] | wt | 5.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.3× (z +10.4) | — |
| [[RPMI-7951 (line)]] | alt | 6.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 1.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.4× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 8.56 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0453× (z -9.4) |
| [[SW1417 (line)]] | alt | 4.93 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0800× (z -8.6) |
| [[SW480 (line)]] | alt | 4.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.75× (z +10.8) | — |
| [[A-172 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16073), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PYGM]] | +0.82 | +0.80 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[TINCR]] | +0.82 | +0.79 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[RFPL3S]] | +0.82 | +0.81 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[CPT1C]] | +0.81 | +0.78 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[SPATA32]] | +0.81 | +0.82 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[VWCE]] | +0.81 | +0.80 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[CPNE9]] | +0.78 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[COL20A1]] | +0.77 | +0.74 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[CHADL]] | +0.76 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[HPX]] | +0.76 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[ATP2A1]] | +0.76 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[MYO15A]] | +0.75 | +0.67 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83E]] | B | FAM83E activity raises SMIM41's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 1.59× lower at baseline in the lines without FAM83E | 0.035 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |
| [[F2]] | B | F2 activity raises SMIM41's level | lines that do not express F2 (11) vs lines expressing it (39) | 1.75× lower at baseline in the lines without F2 | 0.038 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PTPN6]] | B | PTPN6 activity raises SMIM41's level | lines that do not express PTPN6 (8) vs lines expressing it (42) | 1.81× lower at baseline in the lines without PTPN6 | 0.040 | ⚠ within organs, on part of the lines; also absent: LMTK3, ENSG00000257252; maybe low, not absent |
| [[LSMEM2]] | B | LSMEM2 activity raises SMIM41's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 1.59× lower at baseline in the lines without LSMEM2 | 0.051 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[HCN2]] | B | HCN2 activity raises SMIM41's level | lines that do not express HCN2 (6) vs lines expressing it (44) | 1.81× lower at baseline in the lines without HCN2 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000267131, USP31, PRELID3A; maybe low, not absent |
| [[ATG101]] | C | ATG101's natural level strengthens SMIM41's drug response | ATG101's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.27; direction not clear | 0.049 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.831). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.9, -18.1); signed map (15.2, 13.4). **Vector** length 110, 27.2% of its response variance represented; |z| ≥ 3 in 1,072 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +12.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +10.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +4.6 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +4.2 | +3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.6 | +2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.5 | +3.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.5 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +1.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -6.6 | -6.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.9 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.8 | -7.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.2 | -4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.8 | -6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.5 | -5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.0 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.7 | -4.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.7 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.6 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | small integral membrane protein 41 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:52,079,704-52,108,255 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [A0A2R8YCJ5](https://www.uniprot.org/uniprotkb/A0A2R8YCJ5) carries no function annotation.

**Summary**, from NCBI Gene [113523638](https://www.ncbi.nlm.nih.gov/gene/113523638):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:54075](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54075) · Entrez [113523638](https://www.ncbi.nlm.nih.gov/gene/113523638) · UniProt [A0A2R8YCJ5](https://www.uniprot.org/uniprotkb/A0A2R8YCJ5) · Ensembl [ENSG00000284791](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000284791)

## Data

Gene col 16073: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16073); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16073, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16073]; `tensor/DDL_lfc|DDL_z.npy` [16073]; `embed/gene_vectors.npy` [16073]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16073 or target_col == 16073). Every well: [[SMIM41 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/SMIM41.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
