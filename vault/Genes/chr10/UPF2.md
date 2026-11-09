---
symbol: "UPF2"
type: "gene"
col: 7521
ensembl_id: "ENSG00000151461"
name: "UPF2 regulator of nonsense mediated mRNA decay"
location: "10p14"
module: 74
arm: "+"
pooled_cpm: 177.95
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# UPF2

*UPF2 regulator of nonsense mediated mRNA decay* — 10p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.35× (z +10.2, q 2e-21, up in 34 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.30× (z +8.9, q 2e-16, up in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 6 lines (PANC-1 1.78×, HT-29 1.75×, SW480 1.51×, A-427 1.60×, …); [[Homoharringtonine (drug)]] 5 µM in 5 lines (PANC-1 1.76×, NCI-H2347 1.66×, NCI-H460 1.57×, SK-MEL-2 1.64×, …; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H2347 2.04×, PANC-1 1.71×; ⚠ cell-cycle shift, explains ~69% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (PANC-1 1.70×).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.723× (z -11.0, q 3e-25, down in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~23% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.725× (z -10.8, q 7e-25, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TERF2IP]] (+0.68, fdr 1e-05), [[GCC2]] (+0.68, fdr 7e-06), [[RSF1]] (+0.63, fdr 7e-06); moves opposite to [[GLO1]] (-0.63, fdr 9e-06), [[YWHAQ]] (-0.60, fdr 1e-05), [[CORO1C]] (-0.58, fdr 3e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7521.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 6 lines (PANC-1 1.78×, HT-29 1.75×, SW480 1.51×, A-427 1.60×, …); [[Homoharringtonine (drug)]] 5 µM in 5 lines (PANC-1 1.76×, NCI-H2347 1.66×, NCI-H460 1.57×, SK-MEL-2 1.64×, …; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H2347 2.04×, PANC-1 1.71×; ⚠ cell-cycle shift, explains ~69% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (PANC-1 1.70×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +10.2 | 2e-21 | 34/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +8.9 | 2e-16 | 31/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +8.5 | 5e-15 | 33/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.16× | +5.1 | 4e-05 | 22/48 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 1.18× | +4.0 | 0.007 | 13/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.11× | +3.6 | 0.026 | 19/48 (PANC-1, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.07× | +3.1 | 0.14 | 16/48 (PANC-1, NCI-H2347, …) | rises with dose | composition shift |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | 1.09× | +3.1 | 0.15 | 3/48 (HepG2/C3A, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7521.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.723×** | -11.0 | 3e-25 | 37/48 (AsPC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.725×** | -10.8 | 7e-25 | 35/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.712×** | -10.6 | 5e-24 | 33/45 (A-172, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.803×** | -10.5 | 2e-23 | 34/48 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.748×** | -9.8 | 1e-20 | 35/48 (AsPC-1, SW 900, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.798×** | -7.6 | 3e-12 | 31/49 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.802×** | -7.4 | 8e-12 | 35/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **0.810×** | -7.1 | 8e-11 | 29/49 (AsPC-1, SW48, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.805×** | -7.0 | 1e-10 | 24/44 (AsPC-1, SW480, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.834× | -6.1 | 5e-08 | 22/48 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.957× | -5.3 | 5e-06 | 0/50 | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.917× | -4.1 | 0.002 | 10/48 (J82, SNU-423, …) | top dose only | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | 0.889× | -3.8 | 0.006 | 12/48 (AsPC-1, J82, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.822×** | -3.5 | 0.021 | 16/49 (AsPC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~64% of this change | 0.902× | -3.3 | 0.032 | 14/47 (RKO, CFPAC-1, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.909× | -3.2 | 0.044 | 0/49 | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.907× | -3.2 | 0.051 | 7/48 (NCI-H1573, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.911× | -3.1 | 0.051 | 12/48 (LOX-IMVI, COLO 205, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.915× | -3.0 | 0.078 | 7/48 (AsPC-1, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7521. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 322 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.341× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.459× (z -13.7) |
| [[PANC-1 (line)]] | alt | 149 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +15.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.78× (z +11.1) | — |
| [[SW 900 (line)]] | alt | 207 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.464× (z -11.2) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.500× (z -10.1) |
| [[A-427 (line)]] | wt | 185 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.60× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 192 | 0 | 4 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.251× (z -12.7) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 167 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +12.6) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.609× (z -8.6) ⚠ cell-cycle shift, explains ~23% of this change |
| [[A-172 (line)]] | wt | 163 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.504× (z -11.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 253 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.533× (z -10.8) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.537× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 131 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.521× (z -10.5) |
| [[SW480 (line)]] | alt | 199 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.56× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.51× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.448× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[A498 (line)]] | wt | 194 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.517× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[HT-29 (line)]] | alt | 215 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.75× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 231 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.520× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.614× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 216 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.62× (z +9.1) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.507× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[NCI-H460 (line)]] | wt | 117 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +11.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 194 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.588× (z -8.6) ⚠ cell-cycle shift, explains ~20% of this change |
| [[C-33 A (line)]] | alt | 194 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.483× (z -9.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 137 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.447× (z -8.6) ⚠ cell-cycle shift, explains ~23% of this change |
| [[LoVo (line)]] | wt | 177 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.59× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 179 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.377× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[MIA PaCa-2 (line)]] | alt | 207 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.616× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~64% of this change |
| [[NCI-H2030 (line)]] | alt | 212 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.72× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.349× (z -9.2) ⚠ toxic |
| [[RKO (line)]] | wt | 226 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.550× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~64% of this change |
| [[SK-MEL-2 (line)]] | alt | 156 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW48 (line)]] | wt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.410× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[AN3 CA (line)]] | alt | 183 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 67.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 182 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 174 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 168 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 144 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 163 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 130 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 192 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 231 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7521), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERF2IP]] | +0.68 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[GCC2]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[RSF1]] | +0.63 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[ARID4B]] | +0.63 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[TMF1]] | +0.63 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[ARID4A]] | +0.62 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[UBN2]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[SYNRG]] | +0.60 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[SAFB2]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[NKAP]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[PDCD7]] | +0.59 | +0.33 / +0.60 | both halves | 1e-04 |  |
| [[CIR1]] | +0.59 | +0.57 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLO1]] | -0.63 | -0.57 / -0.65 | both halves | 9e-06 |  |
| [[YWHAQ]] | -0.60 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[CORO1C]] | -0.58 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[G3BP1]] | -0.57 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[MAPKAPK3]] | -0.55 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[MPV17L]] | -0.54 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[PFN2]] | -0.54 | -0.52 / -0.39 | both halves | 6e-05 | pathway: Signaling by ROBO receptors |
| [[YWHAG]] | -0.54 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[GOT2]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[PFKM]] | -0.53 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[ATP13A2]] | -0.53 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[GALNT1]] | -0.52 | -0.45 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises UPF2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises UPF2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.2, -45.2); signed map (-12.4, 6.6). **Vector** length 112, 30.8% of its response variance represented; |z| ≥ 3 in 1,017 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.3 | +2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.7 | +8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.3 | +8.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.3 | +0.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.3 | +2.9 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +2.3 | +3.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.3 | -10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.6 | -10.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.2 | -6.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.0 | -7.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -3.1 |
|  | [[Adenine (drug)]] 5 µM |  | -2.8 | -2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -2.2 |
|  | [[Lopinavir (drug)]] 5 µM |  | -2.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | UPF2 regulator of nonsense mediated mRNA decay |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p14 — chr10:11,920,022-12,043,170 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RENT2, DKFZP434D222, KIAA1408, smg-3 |
| Gene groups (HGNC) | DECID complex; MIF4G domain containing proteins |
| Reactome | 7 pathways, smallest: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC); Nonsense-Mediated Decay (NMD); Regulation of expression of SLITs and ROBOs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAU5](https://www.uniprot.org/uniprotkb/Q9HAU5) (Regulator of nonsense transcripts 2):

> Involved in nonsense-mediated decay (NMD) of mRNAs containing premature stop codons by associating with the nuclear exon junction complex (EJC). Recruited by UPF3B associated with the EJC core at the cytoplasmic side of the nuclear envelope and the subsequent formation of an UPF1-UPF2-UPF3 surveillance complex (including UPF1 bound to release factors at the stalled ribosome) is believed to activate NMD. In cooperation with UPF3B stimulates both ATPase and RNA helicase activities of UPF1. Binds …

**Summary**, from NCBI Gene [26019](https://www.ncbi.nlm.nih.gov/gene/26019):

> This gene encodes a protein that is part of a post-splicing multiprotein complex involved in both mRNA nuclear export and mRNA surveillance. mRNA surveillance detects exported mRNAs with truncated open reading frames and initiates nonsense-mediated mRNA decay (NMD). When translation ends upstream from the last exon-exon junction, this triggers NMD to degrade mRNAs containing premature stop codons. This protein is located in the perinuclear area. It interacts with translation release factors and …

**Accessions** — [HGNC:17854](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17854) · Entrez [26019](https://www.ncbi.nlm.nih.gov/gene/26019) · UniProt [Q9HAU5](https://www.uniprot.org/uniprotkb/Q9HAU5) · Ensembl [ENSG00000151461](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151461)

## Data

Gene col 7521: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7521); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7521, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7521]; `tensor/DDL_lfc|DDL_z.npy` [7521]; `embed/gene_vectors.npy` [7521]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7521 or target_col == 7521). Every well: [[UPF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UPF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
