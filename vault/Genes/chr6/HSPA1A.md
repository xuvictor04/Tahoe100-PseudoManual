---
symbol: "HSPA1A"
type: "gene"
col: 12866
ensembl_id: "ENSG00000204389"
name: "heat shock protein family A (Hsp70) member 1A"
location: "6p21.33"
module: 60
arm: "+"
pooled_cpm: 27.77
n_lines_expressing: 37
n_dd_up: 40
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# HSPA1A

*heat shock protein family A (Hsp70) member 1A* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (19 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 114× (z +31.5, q 0e+00, up in 34 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW1417 0.112×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2347 0.207×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSPA1B]] (+0.87, fdr 7e-06, ⚠ same locus), [[SOD1]] (+0.68, fdr 7e-06), [[UBB]] (+0.67, fdr 1e-05), [[HSP90AA2P]] (+0.65, fdr 1e-05); moves opposite to [[TADA3]] (-0.54, fdr 2e-05), [[CHAMP1]] (-0.54, fdr 3e-05), [[DGUOK]] (-0.50, fdr 2e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MSX1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NQO2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 19 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12866.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **114×** | +31.5 | 0e+00 | 34/34 (PANC-1, NCI-H23, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **76.3×** | +28.9 | 0e+00 | 34/34 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **53.5×** | +26.5 | 0e+00 | 34/34 (PANC-1, HT-29, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **51.3×** | +24.8 | 0e+00 | 35/35 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **57.9×** | +14.1 | 3e-43 | 31/31 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **26.1×** | +12.8 | 1e-35 | 35/35 (PANC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **7.14×** | +12.6 | 2e-34 | 34/34 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.38×** | +11.2 | 3e-27 | 32/34 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.70×** | +9.4 | 4e-19 | 32/35 (NCI-H2030, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.71×** | +8.7 | 1e-16 | 32/35 (SNU-423, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **2.42×** | +8.3 | 4e-15 | 24/35 (NCI-H2030, PANC-1, …) | rises with dose | composition shift |
| [[Infigratinib (drug)]] 5 µM |  | **10.7×** | +8.3 | 7e-15 | 34/35 (BT-474, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **3.20×** | +7.7 | 4e-13 | 33/35 (SNU-423, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **3.05×** | +7.4 | 5e-12 | 28/35 (SHP-77, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.80×** | +6.9 | 3e-10 | 33/34 (A549, NCI-H1792, …) | rises with dose |  |
| [[Hydroxyfasudil (drug)]] 0.5 µM |  | **4.71×** | +6.1 | 4e-08 | 30/35 (PANC-1, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **5.25×** | +5.8 | 2e-07 | 26/34 (HT-29, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Pimitespib (drug)]] 0.5 µM |  | **2.86×** | +4.1 | 9e-04 | 24/35 (PANC-1, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +3.9 | 0.002 | 18/34 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[PF-06260933 (drug)]] 0.5 µM |  | **2.33×** | +3.3 | 0.019 | 21/35 (SNU-423, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 5 µM |  | **1.64×** | +3.2 | 0.028 | 15/34 (A498, SW480, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12866.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW1417 0.112×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2347 0.207×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.621× | -3.2 | 0.84 | 16/34 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.67 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12866. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 34.2 | 11 (6 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 121× (z +27.5) | — |
| [[NCI-H460 (line)]] | wt | 21.0 | 10 (6 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 127× (z +20.2) | — |
| [[CFPAC-1 (line)]] | alt | 73.8 | 9 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 48.4× (z +18.9) | — |
| [[A498 (line)]] | wt | 28.2 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 129× (z +22.0) | — |
| [[SHP-77 (line)]] | alt | 52.8 | 8 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 57.3× (z +15.1) | — |
| [[SW1417 (line)]] | alt | 28.8 | 7 (3 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 50.0× (z +19.1) | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 19.1 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 92.5× (z +18.9) | — |
| [[NCI-H2347 (line)]] | alt | 77.5 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 36.6× (z +20.3) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 20.7 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 602× (z +23.4) | — |
| [[SW480 (line)]] | alt | 20.3 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 410× (z +24.6) | — |
| [[A-427 (line)]] | wt | 48.7 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 123× (z +24.3) | — |
| [[C-33 A (line)]] | alt | 28.2 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 88.1× (z +17.9) | — |
| [[HT-29 (line)]] | alt | 43.7 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 107× (z +25.0) | — |
| [[KATO III (line)]] | alt | 16.2 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 108× (z +19.0) | — |
| [[NCI-H1573 (line)]] | alt | 21.7 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 83.2× (z +18.8) | — |
| [[NCI-H23 (line)]] | alt | 72.4 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 148× (z +26.8) | — |
| [[Panc 03.27 (line)]] | alt | 38.4 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 132× (z +22.0) | — |
| [[SW 900 (line)]] | alt | 55.1 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 128× (z +19.2) | — |
| [[A549 (line)]] | wt | 15.1 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 136× (z +17.8) | — |
| [[AsPC-1 (line)]] | alt | 64.0 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 37.8× (z +15.8) | — |
| [[BT-474 (line)]] | alt | 49.1 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 55.1× (z +20.8) | — |
| [[C32 (line)]] | wt | 23.8 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 728× (z +20.4) | — |
| [[HepG2_C3A (line)]] | wt | 78.2 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 26.5× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 18.7× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 11.8 | 5 | 0 | [[Auranofin (drug)]] 5 µM 488× (z +22.4) | — |
| [[Hs 766T (line)]] | wt | 32.9 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 68.3× (z +17.6) | — |
| [[HS-578T (line)]] | alt | 49.9 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 176× (z +18.7) | — |
| [[hTERT-HPNE (line)]] | wt | 21.1 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 399× (z +16.9) | — |
| [[SK-MEL-2 (line)]] | alt | 25.7 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 309× (z +21.8) | — |
| [[LOX-IMVI (line)]] | wt | 32.1 | 4 | 0 | [[Auranofin (drug)]] 5 µM 211× (z +18.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.28 | 4 | 0 | [[Auranofin (drug)]] 5 µM 109× (z +11.8) | — |
| [[NCI-H1792 (line)]] | alt | 15.8 | 4 | 0 | [[Auranofin (drug)]] 5 µM 53.4× (z +12.9) | — |
| [[NCI-H661 (line)]] | alt | 44.7 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 63.3× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 26.9 | 4 | 0 | [[Auranofin (drug)]] 5 µM 347× (z +21.1) | — |
| [[SW 1271 (line)]] | alt | 46.7 | 3 | 0 | [[Auranofin (drug)]] 5 µM 306× (z +12.6) | — |
| [[A-172 (line)]] | wt | 3.29 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.92 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.59 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.65 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.80 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.83 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.96 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.71 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12866), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPA1B]] | +0.87 | +0.81 / +0.87 | both halves | 7e-06 | same gene group; pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 994; ⚠ same locus (9.8 kb, same strand: neighbours can correlate without regulation) |
| [[SOD1]] | +0.68 | +0.62 / +0.73 | both halves | 7e-06 | STRING 440 |
| [[UBB]] | +0.67 | +0.52 / +0.74 | both halves | 1e-05 | pathway: AUF1 (hnRNP D0) binds and destabilizes mRNA; STRING 669 |
| [[HSP90AA2P]] | +0.65 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[HSPB1]] | +0.64 | +0.56 / +0.71 | both halves | 1e-05 | pathway: AUF1 (hnRNP D0) binds and destabilizes mRNA; STRING 977 |
| [[GLA]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[RAD9A]] | +0.61 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[FTL]] | +0.60 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[MED31]] | +0.59 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[HSPE1]] | +0.59 | +0.49 / +0.62 | both halves | 1e-05 | pathway: Mitochondrial unfolded protein response (UPRmt); STRING 814 |
| [[ABHD3]] | +0.57 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[DNAJA1]] | +0.57 | +0.43 / +0.62 | both halves | 3e-05 | pathway: HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; STRING 956 |
| [[PSMB4]] | +0.57 | +0.45 / +0.61 | both halves | 3e-05 | pathway: AUF1 (hnRNP D0) binds and destabilizes mRNA |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TADA3]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[CHAMP1]] | -0.54 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[DGUOK]] | -0.50 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[POLI]] | -0.49 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[GTF3A]] ⚠ | -0.47 | -0.26 / -0.53 | both halves | 4e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[GUF1]] | -0.46 | -0.28 / -0.48 | both halves | 3e-04 |  |
| [[SLC35A5]] | -0.46 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[TMEM128]] | -0.45 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[SF3B3]] | -0.45 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[UBLCP1]] | -0.45 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[CEP135]] | -0.44 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[CEP63]] | -0.44 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[UCHL5]] | -0.43 | -0.24 / -0.49 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSX1]] | B | MSX1 activity lowers HSPA1A's level | lines that do not express MSX1 (6) vs lines expressing it (44) | 2.46× higher at baseline in the lines without MSX1 | 0.071 | ⚠ within organs, on part of the lines; also absent: ANAPC1P4, WDR35, TMCC2; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NQO2]] | B | HSPA1A activity lowers NQO2's level | lines that do not express HSPA1A (13) vs lines expressing it (37) | 1.30× higher at baseline in the lines without HSPA1A | 0.060 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ATP13A3-DT, ZNF569, GCAWKR |

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.627). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-18.1, -10.6); signed map (-24.5, -27.6). **Vector** length 95.1, 26.5% of its response variance represented; |z| ≥ 3 in 969 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Chaperone Mediated Autophagy* (reactome, mean cos +0.51 to 4); *Aggrephagy* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +9.0 | +24.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.7 | +28.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.6 | +26.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.3 | +31.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +6.7 | +14.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.0 | +12.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +1.2 |
|  | [[Infigratinib (drug)]] 5 µM |  | +2.1 | +8.3 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | +0.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.0 | -0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein family A (Hsp70) member 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,815,543-31,817,946 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSP70-1; previously HSPA1 |
| Gene groups (HGNC) | Heat shock 70kDa proteins; TIM23 complex |
| Hallmark sets | COMPLEMENT |
| Reactome | 24 pathways, smallest: Viral RNP Complexes in the Host Cell Nucleus; Mitochondrial unfolded protein response (UPRmt); Attenuation phase |
| Matched by | ensembl_id |

**Function**, from UniProt [P0DMV8](https://www.uniprot.org/uniprotkb/P0DMV8) (Heat shock 70 kDa protein 1A):

> Molecular chaperone implicated in a wide variety of cellular processes, including protection of the proteome from stress, folding and transport of newly synthesized polypeptides, activation of proteolysis of misfolded proteins and the formation and dissociation of protein complexes. Plays a pivotal role in the protein quality control system, ensuring the correct folding of proteins, the re-folding of misfolded proteins and controlling the targeting of proteins for subsequent degradation. This …

**Summary**, from NCBI Gene [3303](https://www.ncbi.nlm.nih.gov/gene/3303):

> This intronless gene encodes a 70kDa heat shock protein which is a member of the heat shock protein 70 family. In conjuction with other heat shock proteins, this protein stabilizes existing proteins against aggregation and mediates the folding of newly translated proteins in the cytosol and in organelles. It is also involved in the ubiquitin-proteasome pathway through interaction with the AU-rich element RNA-binding protein 1. The gene is located in the major histocompatibility complex class …

**Accessions** — [HGNC:5232](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5232) · Entrez [3303](https://www.ncbi.nlm.nih.gov/gene/3303) · UniProt [P0DMV8](https://www.uniprot.org/uniprotkb/P0DMV8) · Ensembl [ENSG00000204389](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204389)

## Data

Gene col 12866: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12866); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12866, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12866]; `tensor/DDL_lfc|DDL_z.npy` [12866]; `embed/gene_vectors.npy` [12866]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12866 or target_col == 12866). Every well: [[HSPA1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSPA1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
