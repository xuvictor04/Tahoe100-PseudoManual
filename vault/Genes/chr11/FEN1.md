---
symbol: "FEN1"
type: "gene"
col: 9661
ensembl_id: "ENSG00000168496"
name: "flap structure-specific endonuclease 1"
location: "11q12.2"
module: 6
arm: "+"
pooled_cpm: 7.95
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 18
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# FEN1

*flap structure-specific endonuclease 1* — 11q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (21 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 3.09× (z +9.5, q 8e-19, up in 29 of 35 measured lines) ⚠ toxic; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.57× (z +5.6, q 3e-06, up in 21 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.587× (z -6.7, q 1e-08, down in 21 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM10]] (+0.88, fdr 7e-06), [[CDC25A]] (+0.86, fdr 7e-06), [[DTL]] (+0.85, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 21 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9661.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **3.09×** | +9.5 | 8e-19 | 29/35 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.83×** | +7.5 | 2e-11 | 29/42 (A549, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **2.15×** | +6.7 | 4e-09 | 28/40 (PANC-1, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.96×** | +5.9 | 6e-07 | 26/44 (PANC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +5.6 | 3e-06 | 21/46 (SW480, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.86×** | +5.4 | 5e-06 | 26/46 (NCI-H2347, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.84×** | +5.3 | 8e-06 | 24/46 (J82, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.81×** | +5.2 | 1e-05 | 25/43 (PANC-1, SW480, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.80×** | +5.2 | 2e-05 | 20/45 (A549, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~85% of this change | **1.73×** | +4.6 | 2e-04 | 10/35 (A549, C32, …) | top dose only |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.42×** | +4.3 | 8e-04 | 18/47 (HT-29, SW480, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.41×** | +4.3 | 1e-03 | 17/45 (PANC-1, SHP-77, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.62×** | +4.1 | 0.002 | 13/43 (SW480, SNU-423, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.60×** | +4.0 | 0.003 | 17/41 (SW480, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.56×** | +3.9 | 0.004 | 16/46 (A549, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +3.7 | 0.007 | 12/44 (LOX-IMVI, SW480, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.018 | 10/45 (A-427, SHP-77, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9661.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.587×** | -6.7 | 1e-08 | 21/39 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.645×** | -5.5 | 1e-05 | 28/46 (MIA PaCa-2, HCT15, …) | rises with dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.679×** | -4.9 | 2e-04 | 17/47 (RKO, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.639×** | -4.0 | 0.010 | 18/42 (A498, HT-29, …) | all doses, flat | position effect removed |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.464×** | -3.8 | 0.018 | 16/46 (A-172, A498, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.658×** | -3.6 | 0.029 | 14/46 (SNU-1, RPMI-7951, …) | all doses, flat | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.670×** | -3.6 | 0.029 | 6/47 (PANC-1, HT-29, …) | all doses, flat | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **0.673×** | -3.5 | 0.030 | 13/45 (Hs 766T, HT-29, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.754×** | -3.5 | 0.031 | 14/44 (A-172, Hs 766T, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.664×** | -3.4 | 0.033 | 19/42 (LS 180, H4, …) | inconsistent across doses | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.684×** | -3.4 | 0.038 | 16/46 (HEC-1-A, LS 180, …) | top dose only | position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.676×** | -3.3 | 0.046 | 14/46 (COLO 205, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.709×** | -3.1 | 0.087 | 8/46 (LOX-IMVI, SW480, …) | inconsistent across doses | position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **0.497×** | -3.1 | 0.087 | 8/45 (A-427, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.702×** | -3.0 | 0.087 | 16/41 (A-172, A498, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.713×** | -3.0 | 0.087 | 11/46 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.789×** | -3.0 | 0.087 | 15/46 (NCI-H1792, PANC-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.41 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9661. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.7 | 1 (1 ⚠) | 1 | [[Topotecan (hydrochloride) (drug)]] 5 µM 6.72× (z +10.2) ⚠ toxic; cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -10.1) |
| [[A-172 (line)]] | wt | 10.2 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0627× (z -10.6) |
| [[A498 (line)]] | wt | 7.55 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -12.6) |
| [[A549 (line)]] | wt | 3.27 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.54× (z +8.7) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[J82 (line)]] | alt | 26.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 8.72 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0766× (z -10.5) |
| [[PANC-1 (line)]] | alt | 6.89 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.88× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | — |
| [[A-427 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9661), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM10]] | +0.88 | +0.90 / +0.85 | both halves | 7e-06 | pathway: DNA Replication; STRING 896 |
| [[CDC25A]] | +0.86 | +0.86 / +0.85 | both halves | 7e-06 | pathway: S Phase; STRING 633 |
| [[DTL]] | +0.85 | +0.85 / +0.81 | both halves | 7e-06 | STRING 731 |
| [[FAM111B]] | +0.83 | +0.78 / +0.85 | both halves | 7e-06 |  |
| [[EXO1]] | +0.82 | +0.86 / +0.80 | both halves | 7e-06 | same gene group; pathway: DNA Double-Strand Break Repair; STRING 901 |
| [[CENPO]] | +0.82 | +0.82 / +0.79 | both halves | 7e-06 | pathway: Chromosome Maintenance |
| [[CDC45]] | +0.82 | +0.87 / +0.77 | both halves | 7e-06 | pathway: DNA Replication; STRING 864 |
| [[GINS2]] | +0.81 | +0.80 / +0.83 | both halves | 7e-06 | pathway: DNA Replication; STRING 741 |
| [[CHAF1A]] | +0.81 | +0.85 / +0.79 | both halves | 7e-06 | STRING 606 |
| [[E2F2]] | +0.81 | +0.76 / +0.82 | both halves | 7e-06 |  |
| [[ZNF367]] | +0.81 | +0.83 / +0.78 | both halves | 7e-06 |  |
| [[CDCA5]] | +0.81 | +0.76 / +0.82 | both halves | 7e-06 | pathway: S Phase; STRING 708 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FEN1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FAM111B]] | B | FAM111B activity raises FEN1's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.61× lower at baseline in the lines without FAM111B | 0.033 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises FEN1's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.90× lower at baseline in the lines without E2F8 | 0.082 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises FEN1's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.82× lower at baseline in the lines without CDC25A | 0.083 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises FEN1's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.76× lower at baseline in the lines without E2F2 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[TP53]] | C | TP53 activity weakens FEN1's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 16 not recorded | the TP53-altered lines respond 1.43× as strongly (z diff -0.84); strongest at Mitoxantrone (dihydrochloride) 5 µM: 1.64x vs 0.94x (z diff -3.0) | 0.709 over the table, 0.044 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.775). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.0, -45.6); signed map (-39.2, -45.4). **Vector** length 97.5, 25.5% of its response variance represented; |z| ≥ 3 in 824 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.58 to 65); *E2F G1/S* (control, mean cos +0.65 to 23); *Cell Cycle Checkpoints* (reactome, mean cos +0.65 to 45).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +4.5 | +5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +4.3 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | +4.1 | +9.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +3.9 | +5.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | +3.7 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +5.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.0 | +1.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.9 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +2.8 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.8 | -6.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -3.6 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -2.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.4 | -4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.2 | +1.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.1 | -4.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.0 | -3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -0.3 |
|  | [[palbociclib (drug)]] 5 µM |  | -1.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | flap structure-specific endonuclease 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.2 — chr11:61,792,911-61,797,238 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FEN-1, MF1; previously RAD2 |
| Gene groups (HGNC) | Rad2/XPG endonuclease family |
| Hallmark sets | DNA_REPAIR, UV_RESPONSE_UP |
| Reactome | 28 pathways, smallest: POLB-Dependent Long Patch Base Excision Repair; Early Phase of HIV Life Cycle; HDR through MMEJ (alt-NHEJ) |
| Matched by | ensembl_id |

**Function**, from UniProt [P39748](https://www.uniprot.org/uniprotkb/P39748) (Flap endonuclease 1):

> Structure-specific nuclease with 5'-flap endonuclease and 5'-3' exonuclease activities involved in DNA replication and repair. During DNA replication, cleaves the 5'-overhanging flap structure that is generated by displacement synthesis when DNA polymerase encounters the 5'-end of a downstream Okazaki fragment. It enters the flap from the 5'-end and then tracks to cleave the flap base, leaving a nick for ligation. Also involved in the long patch base excision repair (LP-BER) pathway, by …

**Summary**, from NCBI Gene [2237](https://www.ncbi.nlm.nih.gov/gene/2237):

> The protein encoded by this gene removes 5' overhanging flaps in DNA repair and processes the 5' ends of Okazaki fragments in lagging strand DNA synthesis. Direct physical interaction between this protein and AP endonuclease 1 during long-patch base excision repair provides coordinated loading of the proteins onto the substrate, thus passing the substrate from one enzyme to another. The protein is a member of the XPG/RAD2 endonuclease family and is one of ten proteins essential for cell-free …

**Accessions** — [HGNC:3650](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3650) · Entrez [2237](https://www.ncbi.nlm.nih.gov/gene/2237) · UniProt [P39748](https://www.uniprot.org/uniprotkb/P39748) · Ensembl [ENSG00000168496](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168496)

## Data

Gene col 9661: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9661); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9661, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9661]; `tensor/DDL_lfc|DDL_z.npy` [9661]; `embed/gene_vectors.npy` [9661]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9661 or target_col == 9661). Every well: [[FEN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FEN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
