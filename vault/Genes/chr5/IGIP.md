---
symbol: "IGIP"
type: "gene"
col: 11315
ensembl_id: "ENSG00000182700"
name: "IgA inducing protein"
location: "5q31.3"
module: 20
arm: "-"
pooled_cpm: 11.21
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 25
n_dd_up_clean: 2
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# IGIP

*IgA inducing protein* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.49× (z +4.8, q 9e-04, up in 20 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.265× (z -15.9, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PURA]] (+0.83, fdr 7e-06, ⚠ same locus), [[FUT11]] (+0.55, fdr 1e-04), [[ALG11]] (+0.53, fdr 1e-05), [[AFTPH]] (+0.53, fdr 3e-05); moves opposite to [[PLCG1]] (-0.54, fdr 1e-05), [[DPP3]] (-0.53, fdr 1e-05), [[STIP1]] (-0.51, fdr 3e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[PURA]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11315.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +4.8 | 9e-04 | 20/47 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.45×** | +4.4 | 0.003 | 14/48 (PANC-1, HOP62, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.34× | +3.4 | 0.15 | 11/46 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.30× | +3.2 | 0.21 | 5/47 (KATO III, NCI-H1573, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.31× | +3.1 | 0.21 | 8/46 (SW480, KATO III, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11315.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.265×** | -15.9 | 0e+00 | 45/47 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.351×** | -11.8 | 9e-30 | 37/45 (SNU-423, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.506×** | -11.5 | 2e-28 | 32/46 (A498, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.376×** | -11.2 | 8e-27 | 39/47 (HOP62, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.396×** | -11.1 | 2e-26 | 38/48 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.172×** | -11.0 | 3e-26 | 42/47 (LOX-IMVI, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.465×** | -9.1 | 5e-18 | 34/45 (LS 180, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.490×** | -8.1 | 3e-14 | 31/48 (HOP62, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.278×** | -8.0 | 8e-14 | 28/44 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.512×** | -7.7 | 8e-13 | 30/47 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.554×** | -6.5 | 3e-09 | 17/27 (A498, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.571×** | -6.4 | 6e-09 | 29/40 (SNU-423, HS-578T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.649×** | -5.2 | 1e-05 | 21/48 (KATO III, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.646×** | -5.0 | 3e-05 | 22/47 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.687×** | -4.5 | 3e-04 | 20/44 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.686×** | -4.3 | 6e-04 | 20/44 (SW 900, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.786×** | -4.1 | 0.001 | 17/48 (A-427, HOP62, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.796×** | -3.8 | 0.004 | 21/47 (C32, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Flumatinib (mesylate) (drug)]] 0.05 µM |  | **0.737×** | -3.4 | 0.021 | 12/46 (NCI-H460, C32, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11315. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 13.5 | 0 | 8 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.164× (z -11.3) |
| [[PANC-1 (line)]] | alt | 16.9 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.298× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.298× (z -10.1) |
| [[HS-578T (line)]] | alt | 13.4 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0960× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.113× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 21.8 | 0 | 4 | — | [[PH-797804 (drug)]] 5 µM 0.0112× (z -15.9) |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0725× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Decitabine (drug)]] 0.5 µM 0.0909× (z -9.8) |
| [[J82 (line)]] | alt | 8.84 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.140× (z -9.7) |
| [[SNU-423 (line)]] | alt | 15.1 | 0 | 4 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0283× (z -18.6) |
| [[C-33 A (line)]] | alt | 13.7 | 0 | 3 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0860× (z -10.5) |
| [[C32 (line)]] | wt | 8.42 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.198× (z -9.5) |
| [[HT-29 (line)]] | alt | 15.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.186× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.192× (z -9.9) |
| [[A-172 (line)]] | wt | 13.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.294× (z -9.2) |
| [[A498 (line)]] | wt | 7.66 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -18.3) |
| [[KATO III (line)]] | alt | 13.7 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.120× (z -11.3) |
| [[LoVo (line)]] | wt | 19.2 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.160× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 5.00 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.150× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 11.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -9.7) |
| [[A-427 (line)]] | wt | 13.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.190× (z -8.9) |
| [[A549 (line)]] | wt | 5.79 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -9.0) |
| [[COLO 205 (line)]] | alt | 21.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -10.3) |
| [[H4 (line)]] | wt | 13.0 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0432× (z -10.7) |
| [[HCT15 (line)]] | alt | 19.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.101× (z -11.1) |
| [[Hs 766T (line)]] | wt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[LOX-IMVI (line)]] | wt | 11.8 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0298× (z -9.9) |
| [[LS 180 (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0513× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 5.76 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0750× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 8.97 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0895× (z -12.3) ⚠ toxic |
| [[RKO (line)]] | wt | 4.54 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0509× (z -9.0) |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -9.6) |
| [[SW480 (line)]] | alt | 9.71 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.259× (z -9.1) |
| [[AN3 CA (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11315), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PURA]] | +0.83 | +0.82 / +0.82 | both halves | 7e-06 | ⚠ same locus (0.3 kb, same strand: neighbours can correlate without regulation) |
| [[FUT11]] | +0.55 | +0.35 / +0.64 | both halves | 1e-04 |  |
| [[ALG11]] | +0.53 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[AFTPH]] | +0.53 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[RSBN1]] | +0.53 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[PWWP2A]] | +0.52 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[ZNF652]] | +0.52 | +0.43 / +0.58 | both halves | 4e-05 |  |
| [[ZNNT1]] | +0.52 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[TERF2IP]] | +0.52 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[KLHL28]] | +0.52 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[DCAF10]] | +0.51 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[MINDY2]] | +0.50 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[MCEE]] | +0.50 | +0.40 / +0.56 | both halves | 5e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLCG1]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[DPP3]] | -0.53 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[STIP1]] | -0.51 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[GPN1]] | -0.50 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[PSMB7]] | -0.49 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[ELAC2]] | -0.49 | -0.40 / -0.54 | both halves | 4e-05 |  |
| [[NIT2]] | -0.49 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[ACOT7]] | -0.49 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[RBM19]] | -0.49 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[YWHAQ]] | -0.48 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[DROSHA]] | -0.48 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[EFTUD2]] | -0.48 | -0.37 / -0.55 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PURA]] | C | IGIP's natural level strengthens PURA's drug response | IGIP's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.57; direction not clear | 1e-03 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.316). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (5.6, -35.8); signed map (-32.8, 26.8). **Vector** length 65.4, 11.3% of its response variance represented; |z| ≥ 3 in 1,113 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.9 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.5 | -4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +4.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.8 | +2.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -5.9 | -15.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | -11.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.0 | -11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | -4.5 | -3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.2 | -2.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.3 | -3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -4.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | IgA inducing protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:140,125,937-140,129,392 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LOC492311; previously C5orf53 |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NJ69](https://www.uniprot.org/uniprotkb/A6NJ69) (IgA-inducing protein homolog):

> Enhances IgA secretion from B-cells stimulated via CD40.

**Summary**, from NCBI Gene [492311](https://www.ncbi.nlm.nih.gov/gene/492311):

> Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33847](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33847) · Entrez [492311](https://www.ncbi.nlm.nih.gov/gene/492311) · UniProt [A6NJ69](https://www.uniprot.org/uniprotkb/A6NJ69) · Ensembl [ENSG00000182700](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182700)

## Data

Gene col 11315: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11315); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11315, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11315]; `tensor/DDL_lfc|DDL_z.npy` [11315]; `embed/gene_vectors.npy` [11315]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11315 or target_col == 11315). Every well: [[IGIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
