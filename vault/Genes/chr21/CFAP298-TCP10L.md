---
symbol: "CFAP298-TCP10L"
type: "gene"
col: 15463
ensembl_id: "ENSG00000265590"
name: "CFAP298-TCP10L readthrough"
location: "21q22.11"
module: 27
arm: "+"
pooled_cpm: 11.21
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 20
n_dd_up_clean: 8
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# CFAP298-TCP10L

*CFAP298-TCP10L readthrough* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +8.1, q 3e-13, up in 24 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.417× (z -11.7, q 5e-29, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCP10L]] (+0.90, fdr 7e-06, ⚠ same locus), [[SEC14L4]] (+0.53, fdr 1e-05), [[LINC03042]] (+0.50, fdr 7e-05), [[NEK5]] (+0.49, fdr 5e-05); moves opposite to [[NANP]] (-0.43, fdr 4e-04), [[DCN]] (-0.41, fdr 3e-04), [[MPI]] (-0.40, fdr 8e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CYS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15463.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +8.1 | 3e-13 | 24/43 (LOX-IMVI, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.45×** | +7.0 | 6e-10 | 20/46 (LoVo, RKO, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +6.1 | 2e-07 | 22/47 (LoVo, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +5.3 | 2e-05 | 4/18 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +5.0 | 6e-05 | 19/45 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +4.4 | 0.001 | 17/47 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.032 | 3/46 (CFPAC-1, A-172, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.050 | 14/42 (LOX-IMVI, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.064 | 5/47 (NCI-H1792, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.065 | 15/45 (KATO III, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15463.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.417×** | -11.7 | 5e-29 | 34/47 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.504×** | -8.8 | 3e-16 | 24/44 (NCI-H460, SW480, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.522×** | -8.7 | 6e-16 | 26/41 (A-427, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.644×** | -8.3 | 1e-14 | 25/43 (HepG2/C3A, SW1417, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.569×** | -7.6 | 4e-12 | 25/45 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.598×** | -6.9 | 5e-10 | 24/46 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.616×** | -6.5 | 7e-09 | 21/42 (HepG2/C3A, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.623×** | -6.4 | 1e-08 | 25/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.630×** | -6.2 | 4e-08 | 21/46 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.751×** | -5.4 | 3e-06 | 19/46 (HepG2/C3A, SW48, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.721×** | -4.4 | 6e-04 | 14/45 (HepG2/C3A, RKO, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.729×** | -4.2 | 0.001 | 14/46 (NCI-H23, CHP-212, …) | two highest doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.588×** | -3.7 | 0.009 | 10/40 (PANC-1, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.683×** | -3.6 | 0.011 | 9/47 (A-172, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.768×** | -3.5 | 0.016 | 12/41 (LS 180, A549, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.606×** | -3.5 | 0.016 | 14/35 (HepG2/C3A, J82, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.774×** | -3.4 | 0.020 | 15/46 (SW480, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.781×** | -3.2 | 0.045 | 13/46 (AsPC-1, H4, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.789×** | -3.2 | 0.045 | 8/46 (AsPC-1, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15463. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 37.1 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0797× (z -18.6) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.110× (z -11.5) |
| [[SW480 (line)]] | alt | 25.5 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0923× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -14.5) |
| [[HOP62 (line)]] | alt | 15.9 | 0 | 4 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0374× (z -10.7) |
| [[A-427 (line)]] | wt | 18.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -10.8) |
| [[H4 (line)]] | wt | 12.6 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0492× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 14.7 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.156× (z -12.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.199× (z -10.8) |
| [[PANC-1 (line)]] | alt | 11.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.230× (z -9.8) |
| [[A-172 (line)]] | wt | 22.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -9.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 4.36 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -8.8) ⚠ cell-cycle shift, explains ~62% of this change |
| [[A549 (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -9.1) ⚠ cell-cycle shift, explains ~62% of this change |
| [[AsPC-1 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.158× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~94% of this change |
| [[C32 (line)]] | wt | 7.84 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0992× (z -9.7) ⚠ toxic |
| [[HS-578T (line)]] | alt | 10.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.46× (z +12.7) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Cytarabine (hydrochloride) (drug)]] 5 µM 0.0506× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 3.82 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0771× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.236× (z -8.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H23 (line)]] | alt | 11.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.119× (z -9.0) |
| [[SW1417 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -10.0) ⚠ cell-cycle shift, explains ~62% of this change |
| [[AN3 CA (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15463), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCP10L]] | +0.90 | +0.91 / +0.89 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SEC14L4]] | +0.53 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[LINC03042]] | +0.50 | +0.37 / +0.52 | both halves | 7e-05 |  |
| [[NEK5]] | +0.49 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[KLHL14]] | +0.46 | +0.48 / +0.27 | both halves | 3e-04 |  |
| [[GCAWKR]] | +0.46 | +0.37 / +0.42 | both halves | 7e-05 |  |
| [[LINC00173]] | +0.45 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[AADACL2-AS1]] | +0.45 | +0.45 / +0.39 | both halves | 5e-05 |  |
| [[SLC30A10]] | +0.44 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[DIO3OS]] | +0.44 | +0.36 / +0.41 | both halves | 1e-04 |  |
| [[SERPIND1]] | +0.44 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[ERICH6-AS1]] | +0.44 | +0.47 / +0.37 | both halves | 9e-05 |  |
| [[LINC02981]] | +0.44 | +0.34 / +0.51 | both halves | 1e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NANP]] | -0.43 | -0.25 / -0.38 | both halves | 4e-04 |  |
| [[DCN]] | -0.41 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[MPI]] | -0.40 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[SLC16A7]] | -0.40 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[FKBP5]] | -0.40 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[CRYBG3]] | -0.39 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[AFG3L2]] | -0.38 | -0.20 / -0.38 | both halves | 7e-04 |  |
| [[FAM106A]] | -0.38 | -0.21 / -0.30 | both halves | 6e-04 |  |
| [[C1GALT1]] | -0.38 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[NNMT]] | -0.37 | -0.23 / -0.46 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYS1]] | B | CYS1 activity raises CFAP298-TCP10L's level | lines that do not express CYS1 (22) vs lines expressing it (28) | 1.80× lower at baseline in the lines without CYS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: MT1A, FMNL1-DT, SEC14L4 |
| [[LYPLAL1-AS1]] | B | LYPLAL1-AS1 activity raises CFAP298-TCP10L's level | lines that do not express LYPLAL1-AS1 (9) vs lines expressing it (41) | 1.54× lower at baseline in the lines without LYPLAL1-AS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000237153, LINC02932, DYNLRB2-AS1; maybe low, not absent |
| [[FGF20]] | B | FGF20 activity raises CFAP298-TCP10L's level | lines that do not express FGF20 (41) vs lines expressing it (9) | 1.53× lower at baseline in the lines without FGF20 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, HEPHL1, GCG |
| [[IGFL4]] | B | IGFL4 activity raises CFAP298-TCP10L's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 1.49× lower at baseline in the lines without IGFL4 | 0.096 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.392). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.4, 40.5); signed map (22.1, 25.2). **Vector** length 67.8, 11.2% of its response variance represented; |z| ≥ 3 in 1,120 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.2 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +0.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +4.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.9 | -7.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -6.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.3 | -8.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -11.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -6.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.0 | -3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -5.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | CFAP298-TCP10L readthrough |
| Locus type | readthrough (other) |
| Location | 21q22.11 — chr21:32,402,511-32,612,865 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10932; previously LINC00846, C21orf77 |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [110091775](https://www.ncbi.nlm.nih.gov/gene/110091775):

> This locus represents naturally occurring readthrough transcription between the neighboring chromosome 21 open reading frame 59 (C21orf59) and TCP10L (t-complex 10 like) genes on chromosome 21. Readthrough transcripts may encode a fusion protein that shares sequence identity with each individual gene product. [provided by RefSeq, Apr 2017]

**Accessions** — [HGNC:54636](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54636) · Entrez [110091775](https://www.ncbi.nlm.nih.gov/gene/110091775) · Ensembl [ENSG00000265590](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000265590)

## Data

Gene col 15463: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15463); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15463, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15463]; `tensor/DDL_lfc|DDL_z.npy` [15463]; `embed/gene_vectors.npy` [15463]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15463 or target_col == 15463). Every well: [[CFAP298-TCP10L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP298-TCP10L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
