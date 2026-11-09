---
symbol: "KIF2A"
type: "gene"
col: 901
ensembl_id: "ENSG00000068796"
name: "kinesin family member 2A"
location: "5q12.1"
module: 18
arm: "+"
pooled_cpm: 138.58
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# KIF2A

*kinesin family member 2A* — 5q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.46× (z +11.8, q 3e-29, up in 36 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.32× (z +9.1, q 2e-17, up in 35 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (AsPC-1 0.436×, A-427 0.562×, J82 0.582×, A-172 0.595×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (Panc 03.27 0.362×, SNU-1 0.375×, A-427 0.562×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Selinexor (drug)]] 5 µM in 2 lines (AsPC-1 0.592×, Hs 766T 0.568×; ⚠ cell-cycle shift, explains ~60% of this change); [[Decitabine (drug)]] 0.05 µM in 1 line (SW48 0.420×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NIN]] (+0.64, fdr 7e-06), [[CSNK1G3]] (+0.61, fdr 1e-05), [[RNF2]] (+0.59, fdr 3e-05); moves opposite to [[MPV17]] (-0.53, fdr 2e-05), [[FLCN]] (-0.53, fdr 1e-05), [[TPP1]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 901.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +11.8 | 3e-29 | 36/47 (NCI-H1792, A-172, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +9.1 | 2e-17 | 35/48 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.26×** | +7.6 | 7e-12 | 28/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.22×** | +6.4 | 2e-08 | 26/48 (CFPAC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.20×** | +6.0 | 2e-07 | 24/48 (SNU-423, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +5.9 | 3e-07 | 22/48 (HS-578T, SW 900, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +5.8 | 4e-07 | 31/49 (NCI-H460, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.16× | +4.9 | 5e-05 | 19/48 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +4.7 | 1e-04 | 11/48 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | 1.12× | +3.6 | 0.015 | 8/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.08× | +3.6 | 0.016 | 5/49 (SW 900, MIA PaCa-2, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.12× | +3.5 | 0.020 | 10/48 (CFPAC-1, NCI-H1792, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.023 | 15/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.11× | +3.4 | 0.029 | 15/48 (SW480, H4, …) | two highest doses |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.08× | +3.3 | 0.032 | 0/49 | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.11× | +3.3 | 0.032 | 11/48 (SW 900, SHP-77, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.11× | +3.1 | 0.052 | 11/47 (NCI-H460, hTERT-HPNE, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 901.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (AsPC-1 0.436×, A-427 0.562×, J82 0.582×, A-172 0.595×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (Panc 03.27 0.362×, SNU-1 0.375×, A-427 0.562×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Selinexor (drug)]] 5 µM in 2 lines (AsPC-1 0.592×, Hs 766T 0.568×; ⚠ cell-cycle shift, explains ~60% of this change); [[Decitabine (drug)]] 0.05 µM in 1 line (SW48 0.420×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -7.9 | 1e-12 | 22/48 (AsPC-1, A-427, …) | top dose only | composition shift |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.844× | -5.5 | 1e-05 | 13/49 (SW480, COLO 205, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 0.888× | -5.4 | 1e-05 | 16/48 (AsPC-1, Hs 766T, …) | all doses, flat | low cells (technical?) |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.896× | -3.5 | 0.056 | 3/48 (SW 900, HEC-1-A, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.896× | -3.4 | 0.074 | 7/49 (SW 900, SW1417, …) | top dose only | plate-row cell shift |
| [[Erlotinib (drug)]] 5 µM |  | 0.901× | -3.2 | 0.100 | 5/47 (KATO III, SW48, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.932× | -3.2 | 0.100 | 6/48 (A-172, RKO, …) | top dose only |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 0.907× | -3.2 | 0.10 | 2/50 (NCI-H1573, NCI-H596) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | 0.908× | -3.1 | 0.10 | 7/48 (LS 180, AsPC-1, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.909× | -3.1 | 0.10 | 7/48 (J82, A-427, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.833× | -3.1 | 0.10 | 10/49 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | 0.935× | -3.1 | 0.10 | 1/48 (SNU-423) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 901. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 172 | 6 (6 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.10× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-172 (line)]] | wt | 184 | 1 (1 ⚠) | 2 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.82× (z +9.2) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.595× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 230 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 198 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -19.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 96.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 159 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.54× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.663× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 238 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 109 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 1.82× (z +8.6) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[COLO 205 (line)]] | alt | 176 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.471× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 109 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.568× (z -10.3) ⚠ cell-cycle shift, explains ~60% of this change |
| [[HS-578T (line)]] | alt | 133 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.572× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 138 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 164 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.582× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 143 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 1.73× (z +8.7) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 97.7 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.63× (z +10.3) ⚠ toxic | — |
| [[NCI-H2030 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.662× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.606× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.362× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 159 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.461× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 153 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.650× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.375× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 128 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.420× (z -8.9) |
| [[A498 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 145 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 167 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 71.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 98.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 148 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 87.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 93.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 165 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 98.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 901), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIN]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 | STRING 837 |
| [[CSNK1G3]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[RNF2]] | +0.59 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[SIMC1]] | +0.59 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[HACD3]] | +0.57 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[KPNA3]] | +0.56 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[GMPS]] | +0.55 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[NSMCE4A]] | +0.55 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[CBL]] | +0.54 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[PALS2]] | +0.53 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[SPAST]] | +0.53 | +0.54 / +0.43 | both halves | 3e-05 | pathway: Mitotic Anaphase; STRING 431 |
| [[CBX3]] | +0.53 | +0.57 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPV17]] | -0.53 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[FLCN]] | -0.53 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[TPP1]] | -0.53 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[TRMO]] | -0.53 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[C1orf43]] | -0.50 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[RBKS]] | -0.50 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[NAPA-AS1]] | -0.50 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[LAMTOR3]] | -0.49 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[CCDC159]] | -0.49 | -0.57 / -0.33 | both halves | 1e-04 |  |
| [[TSC1]] | -0.49 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[SPATA24]] | -0.48 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[VPS11]] | -0.48 | -0.45 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers KIF2A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.385). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-6.5, -4.0); signed map (-20.0, -50.7). **Vector** length 111, 28.3% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +8.8 | +9.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | +8.1 | +6.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +6.2 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | +2.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.8 | +3.6 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +3.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.0 | -7.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -4.6 | -5.4 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.9 | -5.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.8 | -2.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | -3.2 | -3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -2.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[Posaconazole (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.1 | -1.9 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -2.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q12.1 — chr5:62,306,162-62,391,025 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HK2; previously KIF2 |
| Gene groups (HGNC) | Kinesins |
| Hallmark sets | COMPLEMENT, GLYCOLYSIS |
| Reactome | 30 pathways, smallest: Kinesins; Processing of antigen in germinal center B cells; COPI-dependent Golgi-to-ER retrograde traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [O00139](https://www.uniprot.org/uniprotkb/O00139) (Kinesin-like protein KIF2A):

> Plus end-directed microtubule-dependent motor required for normal brain development. May regulate microtubule dynamics during axonal growth. Required for normal progression through mitosis. Required for normal congress of chromosomes at the metaphase plate. Required for normal spindle dynamics during mitosis. Promotes spindle turnover. Implicated in formation of bipolar mitotic spindles. Has microtubule depolymerization activity.

**Summary**, from NCBI Gene [3796](https://www.ncbi.nlm.nih.gov/gene/3796):

> The protein encoded by this gene is a plus end-directed motor required for normal mitotic progression. The encoded protein is required for normal spindle activity during mitosis and is necessary for normal brain development. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:6318](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6318) · Entrez [3796](https://www.ncbi.nlm.nih.gov/gene/3796) · UniProt [O00139](https://www.uniprot.org/uniprotkb/O00139) · Ensembl [ENSG00000068796](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068796)

## Data

Gene col 901: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 901); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 901, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 901]; `tensor/DDL_lfc|DDL_z.npy` [901]; `embed/gene_vectors.npy` [901]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 901 or target_col == 901). Every well: [[KIF2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
