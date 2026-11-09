---
symbol: "GK"
type: "gene"
col: 12687
ensembl_id: "ENSG00000198814"
name: "glycerol kinase"
location: "Xp21.2"
module: 227
arm: "+"
pooled_cpm: 30.51
n_lines_expressing: 46
n_dd_up: 41
n_dd_down: 14
n_dd_up_clean: 34
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/227"]
generated_by: "tahoemap"
---

# GK

*glycerol kinase* — Xp21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.07× (z +12.8, q 7e-35, up in 29 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.640× (z -7.9, q 2e-12, down in 23 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM29]] (+0.56, fdr 3e-05), [[USP53]] (+0.54, fdr 1e-05), [[GRB10]] (+0.53, fdr 3e-05); moves opposite to [[FAM120C]] (-0.51, fdr 3e-05), [[SMPD4]] (-0.49, fdr 4e-05), [[POMK]] (-0.47, fdr 4e-05).
> It is in [[Module 227]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC00520]] → it (grade B ⚠); 2 go from it, the strongest it → [[WIPI1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12687.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.07×** | +12.8 | 7e-35 | 29/43 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.55×** | +12.3 | 2e-32 | 32/43 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.14×** | +10.4 | 6e-23 | 32/44 (SW480, A-172, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.99×** | +9.4 | 6e-19 | 30/44 (A498, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.94×** | +9.1 | 1e-17 | 25/44 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.90×** | +8.8 | 1e-16 | 29/43 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.96×** | +8.7 | 3e-16 | 27/43 (SW480, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +8.0 | 6e-14 | 22/41 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.79×** | +8.0 | 1e-13 | 26/43 (SW480, H4, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +7.6 | 1e-12 | 25/37 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.69×** | +7.2 | 3e-11 | 26/44 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +6.9 | 3e-10 | 24/44 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +6.1 | 6e-08 | 22/43 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +5.8 | 3e-07 | 22/44 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +5.6 | 6e-07 | 22/42 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.2 | 8e-06 | 17/41 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +4.9 | 3e-05 | 20/44 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.41×** | +4.5 | 2e-04 | 17/43 (COLO 205, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12687.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.640×** | -7.9 | 2e-12 | 23/44 (COLO 205, KATO III, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.629×** | -6.1 | 3e-07 | 18/29 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **0.670×** | -5.5 | 9e-06 | 23/44 (BT-474, SW48, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.752×** | -5.1 | 6e-05 | 23/44 (AsPC-1, COLO 205, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.549×** | -4.3 | 0.002 | 17/39 (SW 900, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.570×** | -4.0 | 0.006 | 17/37 (hTERT-HPNE, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 5 µM |  | **0.605×** | -3.6 | 0.027 | 10/44 (SW 900, HepG2/C3A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.774×** | -3.5 | 0.034 | 8/44 (LS 180, HepG2/C3A, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.777×** | -3.4 | 0.036 | 14/44 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.781×** | -3.4 | 0.043 | 17/45 (HepG2/C3A, LoVo, …) | two highest doses |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **0.779×** | -3.2 | 0.065 | 10/43 (CHP-212, LS 180, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.647×** | -3.1 | 0.085 | 15/45 (HepG2/C3A, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.783×** | -3.1 | 0.085 | 16/32 (NCI-H1792, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Omeprazole (drug)]] 5 µM |  | **0.798×** | -3.1 | 0.085 | 4/44 (LS 180, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12687. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 42.8 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.99× (z +13.3) | — |
| [[HepG2_C3A (line)]] | wt | 373 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.377× (z -9.1) |
| [[SW480 (line)]] | alt | 21.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +14.4) | [[Lonafarnib (drug)]] 5 µM 0.137× (z -9.4) ⚠ toxic |
| [[A-172 (line)]] | wt | 36.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -10.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 28.3 | 3 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +12.9) | — |
| [[J82 (line)]] | alt | 24.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.46× (z +16.5) | [[Docetaxel (drug)]] 0.05 µM 0.193× (z -9.6) ⚠ transcription drop; cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 18.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 44.7 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.0437× (z -19.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 65.1 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.64× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 31.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +16.7) | — |
| [[COLO 205 (line)]] | alt | 92.0 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.104× (z -12.4) |
| [[hTERT-HPNE (line)]] | wt | 96.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0556× (z -11.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 26.4 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.190× (z -9.5) |
| [[KATO III (line)]] | alt | 56.4 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.233× (z -11.5) |
| [[LoVo (line)]] | wt | 27.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +12.2) | — |
| [[RKO (line)]] | wt | 16.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +8.5) | — |
| [[A-427 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.62 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 87.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.19 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.90 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12687), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM29]] | +0.56 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[USP53]] | +0.54 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[GRB10]] | +0.53 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[TMEM132B]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[C9orf72]] | +0.53 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[ARG2]] | +0.52 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[ERN1]] | +0.52 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[SPIRE1]] | +0.51 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[NIT1]] | +0.51 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[CSGALNACT2]] | +0.49 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[CDKN1A]] | +0.49 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[SLC25A37]] | +0.49 | +0.42 / +0.50 | both halves | 4e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM120C]] | -0.51 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[SMPD4]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[POMK]] | -0.47 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[GTF2I]] | -0.46 | -0.32 / -0.52 | both halves | 1e-04 |  |
| [[ERBB2]] | -0.46 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[PTGFRN]] | -0.46 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[RAE1]] | -0.45 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[GUSBP2-1]] | -0.45 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[ZZZ3]] | -0.45 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[SETD4]] | -0.44 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[DIDO1]] | -0.44 | -0.36 / -0.38 | both halves | 9e-05 |  |
| [[ZMYM3]] | -0.44 | -0.38 / -0.49 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00520]] | B | LINC00520 activity raises GK's level | lines that do not express LINC00520 (31) vs lines expressing it (19) | 1.62× lower at baseline in the lines without LINC00520 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, LINC00589, LINC02930 |
| [[TOP2A]] | B | TOP2A activity lowers GK's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WIPI1]] | C | GK activity raises WIPI1's level | lines that do not express GK (4) vs lines expressing it (46) | 2.55× lower at baseline in the lines without GK | 0.042 | ⚠ few lines (4 vs 46); across organs; maybe low, not absent |
| [[ARFGAP3]] | C | GK activity raises ARFGAP3's level | lines that do not express GK (4) vs lines expressing it (46) | 1.74× lower at baseline in the lines without GK | 0.050 | ⚠ few lines (4 vs 46); across organs; maybe low, not absent |

## Where it sits

- **Module**: [[Module 227]]; 9 genes; every member is in the + arm (projection on the module's main direction 0.656). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.2, -6.6); signed map (39.9, 15.0). **Vector** length 112, 29.2% of its response variance represented; |z| ≥ 3 in 1,301 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.5 | -2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | -6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.5 | +4.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.5 | +12.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +4.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.8 | +2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.3 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +3.6 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -5.9 | -4.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.5 | -7.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -2.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.6 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -5.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.2 | -1.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.8 | -3.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | glycerol kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp21.2 — chrX:30,653,359-30,731,462 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GK1, GKD |
| Gene groups (HGNC) | Glycerol kinase family; FGGY kinase family |
| Reactome | 3 pathways, smallest: Triglyceride biosynthesis; Triglyceride metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [P32189](https://www.uniprot.org/uniprotkb/P32189) (Glycerol kinase):

> Kinase that plays a key role in glycerol metabolism, catalyzing its phosphorylation to produce sn-glycerol 3-phosphate. Sn-glycerol 3-phosphate is a crucial intermediate in various metabolic pathways, such as the synthesis of glycerolipids and triglycerides, glycogenesis, glycolysis and gluconeogenesis.

**Summary**, from NCBI Gene [2710](https://www.ncbi.nlm.nih.gov/gene/2710):

> The protein encoded by this gene belongs to the FGGY kinase family. This protein is a key enzyme in the regulation of glycerol uptake and metabolism. It catalyzes the phosphorylation of glycerol by ATP, yielding ADP and glycerol-3-phosphate. Mutations in this gene are associated with glycerol kinase deficiency (GKD). Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:4289](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4289) · Entrez [2710](https://www.ncbi.nlm.nih.gov/gene/2710) · UniProt [P32189](https://www.uniprot.org/uniprotkb/P32189) · Ensembl [ENSG00000198814](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198814)

## Data

Gene col 12687: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12687); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12687, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12687]; `tensor/DDL_lfc|DDL_z.npy` [12687]; `embed/gene_vectors.npy` [12687]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12687 or target_col == 12687). Every well: [[GK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
