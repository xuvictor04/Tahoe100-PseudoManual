---
symbol: "VIM-AS1"
type: "gene"
col: 13692
ensembl_id: "ENSG00000229124"
name: "VIM antisense RNA 1"
location: "10p13"
module: 26
arm: "+"
pooled_cpm: 6.74
n_lines_expressing: 44
n_dd_up: 17
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# VIM-AS1

*VIM antisense RNA 1* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.97× (z +14.2, q 6e-43, up in 21 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.592× (z -7.8, q 4e-12, down in 21 of 40 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP3K7CL]] (+0.55, fdr 1e-05), [[NIPBL-DT]] (+0.54, fdr 7e-05), [[ALDH1A3]] (+0.54, fdr 5e-05); moves opposite to [[TTC38]] (-0.52, fdr 6e-05), [[CIAO3]] (-0.49, fdr 6e-05), [[SEPTIN7P2]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[LAMC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13692.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +14.2 | 6e-43 | 21/37 (NCI-H460, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.29×** | +11.8 | 8e-30 | 8/12 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +9.1 | 3e-17 | 15/25 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +8.5 | 2e-15 | 18/40 (A-427, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +7.9 | 3e-13 | 7/15 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +7.1 | 1e-10 | 15/40 (A-427, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.9 | 3e-07 | 14/35 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +5.0 | 4e-05 | 11/40 (LoVo, KATO III, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.4 | 6e-04 | 15/34 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fumaric acid (drug)]] 0.5 µM |  | **1.34×** | +4.4 | 7e-04 | 4/41 (A498, PANC-1, …) | two highest doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.010 | 3/39 (NCI-H23, CFPAC-1, …) | top dose only |  |
| [[DTP3 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +3.6 | 0.013 | 6/41 (PANC-1, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Dexmedetomidine (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.020 | 6/39 (SNU-423, HOP62, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.026 | 5/39 (C32, RKO, …) | inconsistent across doses |  |
| [[Decitabine (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.031 | 2/38 (NCI-H460, A498) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.039 | 5/41 (J82, PANC-1, …) | top dose only |  |
| [[Larotrectinib (drug)]] 5 µM |  | 1.16× | +3.1 | 0.055 | 4/40 (NCI-H460, HOP62, …) | top dose only |  |
| [[Fumaric acid (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.082 | 2/41 (NCI-H2030, NCI-H1573) | two highest doses | plate-row cell shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13692.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.592×** | -7.8 | 4e-12 | 21/40 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.651×** | -6.0 | 5e-07 | 16/37 (Hs 766T, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.683×** | -5.7 | 3e-06 | 19/38 (J82, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.686×** | -5.6 | 3e-06 | 13/41 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.689×** | -5.5 | 4e-06 | 19/34 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.797×** | -4.8 | 2e-04 | 14/36 (SK-MEL-2, NCI-H23, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.748×** | -4.3 | 0.001 | 13/39 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.767×** | -4.0 | 0.005 | 8/41 (RKO, SW 1271, …) | inconsistent across doses |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **0.777×** | -3.6 | 0.020 | 2/41 (SNU-423, NCI-H661) | top dose only | plate-row cell shift |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | 0.860× | -3.2 | 0.086 | 5/38 (HEC-1-A, RPMI-7951, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.863× | -3.1 | 0.10 | 4/41 (NCI-H23, Hs 766T, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13692. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 32.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 20.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -16.0) ⚠ cell-cycle shift, explains ~24% of this change |
| [[A549 (line)]] | wt | 3.84 | 0 | 1 | — | [[Ligustrazine (drug)]] 5 µM 0.0843× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 6.60 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0860× (z -9.5) |
| [[BT-474 (line)]] | alt | 5.25 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0531× (z -8.8) ⚠ cell-cycle shift, explains ~58% of this change |
| [[C32 (line)]] | wt | 6.69 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0786× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 5.35 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -8.5) ⚠ cell-cycle shift, explains ~24% of this change |
| [[MIA PaCa-2 (line)]] | alt | 6.95 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0782× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 4.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 6.15 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.114× (z -10.3) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 3.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 9.11 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -9.6) ⚠ cell-cycle shift, explains ~24% of this change |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.1000× (z -16.1) ⚠ cell-cycle shift, explains ~24% of this change |
| [[SW480 (line)]] | alt | 7.82 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -9.6) ⚠ cell-cycle shift, explains ~24% of this change |
| [[A-172 (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13692), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP3K7CL]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[NIPBL-DT]] | +0.54 | +0.37 / +0.48 | both halves | 7e-05 |  |
| [[ALDH1A3]] | +0.54 | +0.59 / +0.39 | both halves | 5e-05 |  |
| [[ZNF514]] | +0.54 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[BHLHE40-AS1]] | +0.54 | +0.39 / +0.52 | both halves | 6e-05 | same gene group |
| [[DOCK2]] | +0.52 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[MSL3]] | +0.51 | +0.39 / +0.43 | both halves | 6e-05 |  |
| [[HSDL2-AS1]] | +0.51 | +0.37 / +0.35 | both halves | 1e-04 | same gene group |
| [[TRDMT1]] | +0.50 | +0.41 / +0.57 | both halves | 4e-05 | ⚠ same locus (12.2 kb, same strand: neighbours can correlate without regulation) |
| [[EPB41L2]] | +0.50 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[PLEKHA8P1]] | +0.49 | +0.34 / +0.31 | both halves | 2e-04 |  |
| [[CCNT2-AS1]] | +0.49 | +0.22 / +0.51 | both halves | 6e-04 | same gene group |
| [[SAXO1]] | +0.49 | +0.37 / +0.40 | both halves | 9e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC38]] | -0.52 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[CIAO3]] | -0.49 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[SEPTIN7P2]] | -0.49 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[CAPN7]] | -0.49 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[MBD4]] | -0.47 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[MPHOSPH10]] | -0.47 | -0.32 / -0.49 | both halves | 1e-04 |  |
| [[PUS3]] | -0.47 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[USP42]] | -0.46 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[RBMX2]] | -0.43 | -0.29 / -0.42 | both halves | 2e-04 |  |
| [[NMT1]] | -0.43 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[LSM2]] | -0.43 | -0.27 / -0.37 | both halves | 3e-04 |  |
| [[C18orf21]] | -0.42 | -0.29 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers VIM-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PGM5P2-1]] | B | PGM5P2-1 activity raises VIM-AS1's level | lines that do not express PGM5P2-1 (12) vs lines expressing it (38) | 1.91× lower at baseline in the lines without PGM5P2-1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MAMLD1, HRH1; maybe low, not absent |
| [[PGM5P2]] | B | PGM5P2 activity raises VIM-AS1's level | lines that do not express PGM5P2 (9) vs lines expressing it (41) | 1.83× lower at baseline in the lines without PGM5P2 | 0.076 | ⚠ within organs, on part of the lines; also absent: PGM5P2-1, PALM2AKAP2, FKBP7; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises VIM-AS1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMC1]] | B | VIM-AS1 activity raises LAMC1's level | lines that do not express VIM-AS1 (6) vs lines expressing it (44) | 3.26× lower at baseline in the lines without VIM-AS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000290876, SCHIP1, BLVRA; maybe low, not absent |
| [[EPB41L2]] | B | VIM-AS1 activity raises EPB41L2's level | lines that do not express VIM-AS1 (6) vs lines expressing it (44) | 2.48× lower at baseline in the lines without VIM-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000290876, SCHIP1, BLVRA; maybe low, not absent |
| [[FLNA]] | B | VIM-AS1 activity raises FLNA's level | lines that do not express VIM-AS1 (6) vs lines expressing it (44) | 2.73× lower at baseline in the lines without VIM-AS1 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000290876, SCHIP1, BLVRA; maybe low, not absent |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.379). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (15.0, 18.8); signed map (27.6, -1.0). **Vector** length 56.7, 8.06% of its response variance represented; |z| ≥ 3 in 933 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +7.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.9 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +11.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +8.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | -0.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.2 | -7.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.6 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -5.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -4.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.6 | -2.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -3.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -1.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | VIM antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10p13 — chr10:17,214,239-17,230,018 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44879](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44879) · Entrez [100507347](https://www.ncbi.nlm.nih.gov/gene/100507347) · Ensembl [ENSG00000229124](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229124)

## Data

Gene col 13692: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13692); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13692, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13692]; `tensor/DDL_lfc|DDL_z.npy` [13692]; `embed/gene_vectors.npy` [13692]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13692 or target_col == 13692). Every well: [[VIM-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VIM-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
