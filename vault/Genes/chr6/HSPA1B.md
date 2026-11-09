---
symbol: "HSPA1B"
type: "gene"
col: 12865
ensembl_id: "ENSG00000204388"
name: "heat shock protein family A (Hsp70) member 1B"
location: "6p21.33"
module: 60
arm: "+"
pooled_cpm: 25.03
n_lines_expressing: 50
n_dd_up: 45
n_dd_down: 0
n_dd_up_clean: 27
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# HSPA1B

*heat shock protein family A (Hsp70) member 1B* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (18 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 77.1× (z +38.7, q 0e+00, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.153×, NCI-H2347 0.226×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.160×; ⚠ cell-cycle shift, explains ~50% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.268×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change); [[Hydroxyurea (drug)]] 0.5 µM in 1 line (A549 0.0932×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSPA1A]] (+0.87, fdr 7e-06, ⚠ same locus), [[HSP90AA2P]] (+0.74, fdr 7e-06), [[SOD1]] (+0.74, fdr 7e-06), [[HSPE1]] (+0.69, fdr 7e-06); moves opposite to [[TADA3]] (-0.59, fdr 1e-05), [[CHAMP1]] (-0.59, fdr 1e-05), [[DGUOK]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[KRT16]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12865.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **77.1×** | +38.7 | 0e+00 | 48/48 (LoVo, HT-29, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **49.5×** | +34.8 | 0e+00 | 47/47 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **35.9×** | +31.9 | 0e+00 | 48/48 (HT-29, KATO III, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **29.2×** | +28.4 | 0e+00 | 48/48 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **17.9×** | +18.3 | 0e+00 | 48/49 (PANC-1, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **34.2×** | +16.5 | 0e+00 | 39/39 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **6.47×** | +16.0 | 0e+00 | 43/45 (COLO 205, C32, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.41×** | +10.6 | 2e-24 | 45/49 (NCI-H2347, HT-29, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.14×** | +10.2 | 1e-22 | 45/48 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **3.13×** | +10.2 | 2e-22 | 47/48 (SNU-423, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.82×** | +9.2 | 2e-18 | 44/48 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Infigratinib (drug)]] 5 µM |  | **6.63×** | +8.8 | 6e-17 | 45/46 (KATO III, HEC-1-A, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.66×** | +8.7 | 1e-16 | 40/46 (KATO III, SHP-77, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.97×** | +8.5 | 5e-16 | 30/46 (A498, C32, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.45×** | +8.0 | 6e-14 | 36/48 (SHP-77, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.19×** | +7.0 | 1e-10 | 35/48 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +6.9 | 1e-10 | 33/46 (NCI-H2030, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **3.90×** | +6.3 | 7e-09 | 33/43 (KATO III, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.98×** | +6.1 | 3e-08 | 33/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.98×** | +5.8 | 2e-07 | 27/48 (HEC-1-A, A-172, …) | top dose only | position effect removed |
| [[Hydroxyfasudil (drug)]] 0.5 µM |  | **2.43×** | +5.6 | 5e-07 | 37/48 (PANC-1, HOP62, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12865.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.153×, NCI-H2347 0.226×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.160×; ⚠ cell-cycle shift, explains ~50% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.268×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change); [[Hydroxyurea (drug)]] 0.5 µM in 1 line (A549 0.0932×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.777× | -3.2 | 0.45 | 14/48 (RKO, A-427, …) | rises with dose | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | 0.704× | -3.2 | 0.45 | 15/48 (A-427, RKO, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12865. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 35.6 | 8 (3 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 74.5× (z +25.2) | [[Dinaciclib (drug)]] 5 µM 0.153× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[NCI-H2347 (line)]] | alt | 68.1 | 7 (2 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 20.2× (z +20.2) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[A-427 (line)]] | wt | 25.2 | 7 (2 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 88.3× (z +26.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -10.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A498 (line)]] | wt | 22.6 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 61.0× (z +20.8) | — |
| [[CFPAC-1 (line)]] | alt | 49.1 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 31.8× (z +18.7) | — |
| [[SHP-77 (line)]] | alt | 20.7 | 8 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 31.7× (z +13.4) | — |
| [[SK-MEL-2 (line)]] | alt | 20.9 | 8 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 211× (z +22.3) | — |
| [[SNU-423 (line)]] | alt | 13.8 | 8 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 278× (z +23.2) | — |
| [[A-172 (line)]] | wt | 16.3 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 210× (z +22.0) | — |
| [[C32 (line)]] | wt | 19.5 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 259× (z +22.4) | — |
| [[HEC-1-A (line)]] | alt | 18.1 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 184× (z +23.8) | — |
| [[HT-29 (line)]] | alt | 43.3 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 66.3× (z +27.9) | — |
| [[LoVo (line)]] | wt | 27.5 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 114× (z +28.4) | — |
| [[LS 180 (line)]] | wt | 26.9 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 32.4× (z +19.2) | — |
| [[NCI-H460 (line)]] | wt | 13.6 | 7 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 83.2× (z +19.9) | — |
| [[SW1417 (line)]] | alt | 43.7 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 28.5× (z +18.0) | — |
| [[SW480 (line)]] | alt | 15.4 | 7 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 217× (z +25.5) | — |
| [[A549 (line)]] | wt | 8.28 | 5 | 1 | [[Ixazomib citrate (drug)]] 5 µM 70.6× (z +15.6) | [[Hydroxyurea (drug)]] 0.5 µM 0.0932× (z -8.6) |
| [[C-33 A (line)]] | alt | 30.7 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 93.8× (z +20.8) | — |
| [[HOP62 (line)]] | alt | 15.3 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 399× (z +24.2) | — |
| [[J82 (line)]] | alt | 41.1 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 97.4× (z +20.8) | — |
| [[NCI-H1573 (line)]] | alt | 12.8 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 29.9× (z +15.4) | — |
| [[NCI-H1792 (line)]] | alt | 11.6 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 30.8× (z +12.9) | — |
| [[NCI-H2030 (line)]] | alt | 29.4 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 48.6× (z +19.8) | — |
| [[NCI-H23 (line)]] | alt | 38.0 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 160× (z +26.3) | — |
| [[Panc 03.27 (line)]] | alt | 29.2 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 76.7× (z +23.2) | — |
| [[PANC-1 (line)]] | alt | 16.2 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 83.2× (z +26.7) | — |
| [[SW 900 (line)]] | alt | 27.6 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 69.8× (z +16.3) | — |
| [[SW48 (line)]] | wt | 40.4 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 130× (z +20.4) | — |
| [[COLO 205 (line)]] | alt | 22.1 | 5 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 55.4× (z +15.5) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 40.9× (z +14.9) | — |
| [[Hs 766T (line)]] | wt | 19.3 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 43.3× (z +17.2) | — |
| [[HS-578T (line)]] | alt | 26.0 | 5 | 0 | [[Auranofin (drug)]] 5 µM 126× (z +17.6) | — |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 217× (z +16.0) | — |
| [[LOX-IMVI (line)]] | wt | 16.1 | 5 | 0 | [[Auranofin (drug)]] 5 µM 128× (z +19.2) | — |
| [[RKO (line)]] | wt | 23.9 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 66.7× (z +19.5) | — |
| [[AsPC-1 (line)]] | alt | 35.7 | 4 | 0 | [[Auranofin (drug)]] 5 µM 24.7× (z +14.5) | — |
| [[BT-474 (line)]] | alt | 31.7 | 4 | 0 | [[Auranofin (drug)]] 5 µM 48.6× (z +20.0) | — |
| [[H4 (line)]] | wt | 10.9 | 4 | 0 | [[Auranofin (drug)]] 5 µM 300× (z +15.6) | — |
| [[HCT15 (line)]] | alt | 36.4 | 4 | 0 | [[Auranofin (drug)]] 5 µM 48.2× (z +18.1) | — |
| [[HepG2_C3A (line)]] | wt | 54.0 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 22.5× (z +10.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 14.8× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.04 | 4 | 0 | [[Auranofin (drug)]] 5 µM 236× (z +15.6) | — |
| [[RPMI-7951 (line)]] | alt | 16.3 | 4 | 0 | [[Auranofin (drug)]] 5 µM 232× (z +19.8) | — |
| [[CHP-212 (line)]] | wt | 23.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 54.6× (z +9.6) | — |
| [[SW 1271 (line)]] | alt | 28.5 | 3 | 0 | [[Auranofin (drug)]] 5 µM 207× (z +11.0) | — |
| [[AN3 CA (line)]] | alt | 23.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 178× (z +15.4) | — |
| [[SNU-1 (line)]] | wt | 8.02 | 1 | 0 | [[Auranofin (drug)]] 5 µM 130× (z +12.4) | — |
| [[NCI-H2122 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12865), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPA1A]] | +0.87 | +0.81 / +0.87 | both halves | 7e-06 | same gene group; pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 994; ⚠ same locus (9.8 kb, same strand: neighbours can correlate without regulation) |
| [[HSP90AA2P]] | +0.74 | +0.68 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[SOD1]] | +0.74 | +0.69 / +0.77 | both halves | 7e-06 | STRING 453 |
| [[HSPE1]] | +0.69 | +0.61 / +0.72 | both halves | 7e-06 | pathway: Mitochondrial unfolded protein response (UPRmt); STRING 845 |
| [[HSPB1]] | +0.69 | +0.67 / +0.70 | both halves | 7e-06 | pathway: Attenuation phase; STRING 939 |
| [[HSP90AA1]] | +0.69 | +0.62 / +0.74 | both halves | 7e-06 | pathway: Attenuation phase; STRING 998 |
| [[CACYBP]] | +0.67 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[DNAJA1]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 | pathway: HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; STRING 984 |
| [[FTL]] | +0.64 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[DNAJB1]] | +0.63 | +0.62 / +0.74 | both halves | 7e-06 | pathway: Attenuation phase; STRING 998 |
| [[GLA]] | +0.63 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[HSP90AB2P]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[HSP90AB3P]] | +0.63 | +0.53 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TADA3]] | -0.59 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[CHAMP1]] | -0.59 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[DGUOK]] | -0.58 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[CEP135]] | -0.57 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[POLI]] | -0.55 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[PPP3CB]] | -0.54 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[DDX18]] | -0.53 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[DOP1A]] | -0.51 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[UBLCP1]] | -0.50 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[CEP63]] | -0.49 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[RSPRY1]] | -0.49 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[RB1]] | -0.48 | -0.47 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT16]] | B | KRT16 activity raises HSPA1B's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 1.43× lower at baseline in the lines without KRT16 | 0.023 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[B4GALNT1]] | B | B4GALNT1 activity lowers HSPA1B's level | lines that do not express B4GALNT1 (16) vs lines expressing it (34) | 1.50× higher at baseline in the lines without B4GALNT1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.767). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-18.3, -10.8); signed map (-24.7, -27.8). **Vector** length 102, 29.7% of its response variance represented; |z| ≥ 3 in 1,366 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Chaperone Mediated Autophagy* (reactome, mean cos +0.60 to 4); *Aggrephagy* (reactome, mean cos +0.54 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +11.0 | +28.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +11.0 | +38.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +10.8 | +34.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.0 | +31.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +8.9 | +16.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +6.2 | +18.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +1.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -5.7 | +1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | +1.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | +1.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -4.5 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -0.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.0 | -0.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.8 | -0.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein family A (Hsp70) member 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,827,738-31,830,254 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSP70-2 |
| Gene groups (HGNC) | Heat shock 70kDa proteins; TIM23 complex |
| Reactome | 18 pathways, smallest: Mitochondrial unfolded protein response (UPRmt); Attenuation phase; HSF1 activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P0DMV9](https://www.uniprot.org/uniprotkb/P0DMV9) (Heat shock 70 kDa protein 1B):

> Molecular chaperone implicated in a wide variety of cellular processes, including protection of the proteome from stress, folding and transport of newly synthesized polypeptides, activation of proteolysis of misfolded proteins and the formation and dissociation of protein complexes. Plays a pivotal role in the protein quality control system, ensuring the correct folding of proteins, the re-folding of misfolded proteins and controlling the targeting of proteins for subsequent degradation. This …

**Summary**, from NCBI Gene [3304](https://www.ncbi.nlm.nih.gov/gene/3304):

> This intronless gene encodes a 70kDa heat shock protein which is a member of the heat shock protein 70 family. In conjuction with other heat shock proteins, this protein stabilizes existing proteins against aggregation and mediates the folding of newly translated proteins in the cytosol and in organelles. It is also involved in the ubiquitin-proteasome pathway through interaction with the AU-rich element RNA-binding protein 1. The gene is located in the major histocompatibility complex class …

**Accessions** — [HGNC:5233](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5233) · Entrez [3304](https://www.ncbi.nlm.nih.gov/gene/3304) · UniProt [P0DMV9](https://www.uniprot.org/uniprotkb/P0DMV9) · Ensembl [ENSG00000204388](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204388)

## Data

Gene col 12865: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12865); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12865, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12865]; `tensor/DDL_lfc|DDL_z.npy` [12865]; `embed/gene_vectors.npy` [12865]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12865 or target_col == 12865). Every well: [[HSPA1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSPA1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
