---
symbol: "SDHD"
type: "gene"
col: 12858
ensembl_id: "ENSG00000204370"
name: "succinate dehydrogenase complex subunit D"
location: "11q23.1"
module: 20
arm: "+"
pooled_cpm: 32.74
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# SDHD

*succinate dehydrogenase complex subunit D* — 11q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.78× (z +19.4, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.861× (z -5.0, q 3e-04, down in 20 of 47 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[PF-06260933 (drug)]] 5 µM: 0.737× (z -3.8, q 0.025, down in 15 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (HCT15 0.128×; ⚠ toxic; transcription drop); [[Furosemide (drug)]] 0.5 µM in 1 line (CHP-212 0.0768×); [[Ritonavir (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.256×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (NCI-H460 0.404×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1D]] (+0.78, fdr 7e-06), [[NAXD]] (+0.66, fdr 1e-05), [[EIF3F]] (+0.64, fdr 7e-06); moves opposite to [[N4BP3]] (-0.62, fdr 1e-05), [[JUND]] (-0.56, fdr 3e-05), [[PAOX]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12858.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +19.4 | 0e+00 | 44/48 (NCI-H2347, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +12.3 | 1e-32 | 34/48 (Panc 03.27, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +9.7 | 7e-20 | 26/41 (NCI-H23, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +9.1 | 2e-17 | 25/47 (MIA PaCa-2, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +8.2 | 4e-14 | 30/48 (PANC-1, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.35×** | +7.1 | 9e-11 | 30/44 (MIA PaCa-2, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.35×** | +6.9 | 3e-10 | 20/37 (J82, LoVo, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +6.4 | 1e-08 | 27/48 (PANC-1, LOX-IMVI, …) | two highest doses | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.54×** | +5.4 | 5e-06 | 14/35 (HT-29, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.24×** | +5.2 | 1e-05 | 19/48 (SNU-1, SW48, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +5.1 | 2e-05 | 17/48 (PANC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.23×** | +5.0 | 3e-05 | 19/48 (PANC-1, HepG2/C3A, …) | two highest doses | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.23×** | +4.9 | 4e-05 | 19/48 (Hs 766T, NCI-H2347, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.43×** | +4.5 | 3e-04 | 16/48 (KATO III, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.20× | +4.3 | 7e-04 | 17/48 (SW48, LS 180, …) | rises with dose | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.39×** | +4.1 | 0.001 | 9/47 (KATO III, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.16× | +3.6 | 0.010 | 20/48 (HT-29, SW480, …) | top dose only |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.016 | 8/47 (COLO 205, LoVo, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.021 | 9/48 (SNU-1, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.035 | 5/48 (PANC-1, NCI-H2347, …) | rises with dose | position effect removed |
| [[Adenine (drug)]] 5 µM |  | 1.10× | +3.1 | 0.047 | 5/48 (J82, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | 1.10× | +3.1 | 0.047 | 1/48 (PANC-1) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.26×** | +2.9 | 0.079 | 9/48 (KATO III, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12858.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (HCT15 0.128×; ⚠ toxic; transcription drop); [[Furosemide (drug)]] 0.5 µM in 1 line (CHP-212 0.0768×); [[Ritonavir (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.256×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (NCI-H460 0.404×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.861× | -5.0 | 3e-04 | 20/47 (NCI-H2347, CFPAC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.807×** | -4.9 | 3e-04 | 22/48 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **0.737×** | -3.8 | 0.025 | 15/48 (Hs 766T, NCI-H1573, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.953× | -3.8 | 0.025 | 1/48 (CHP-212) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.856× | -3.7 | 0.025 | 9/48 (SW 1271, AsPC-1, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.911× | -3.1 | 0.17 | 5/48 (NCI-H23, C32, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12858. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 25.8 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 36.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 29.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +13.2) | — |
| [[NCI-H2347 (line)]] | alt | 43.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +15.0) | — |
| [[Panc 03.27 (line)]] | alt | 36.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 51.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 40.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 22.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +10.1) | — |
| [[CHP-212 (line)]] | wt | 27.8 | 0 | 1 | — | [[Furosemide (drug)]] 0.5 µM 0.0768× (z -10.0) |
| [[HCT15 (line)]] | alt | 36.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -12.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 18.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 28.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +11.4) | — |
| [[hTERT-HPNE (line)]] | wt | 32.3 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.256× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 43.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +14.0) | — |
| [[NCI-H23 (line)]] | alt | 28.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.20× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 21.7 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.404× (z -9.3) |
| [[SW 900 (line)]] | alt | 29.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +9.3) | — |
| [[SW1417 (line)]] | alt | 44.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +10.1) | — |
| [[SW48 (line)]] | wt | 39.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 40.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12858), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1D]] | +0.78 | +0.69 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[NAXD]] | +0.66 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[EIF3F]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[ZBTB26]] | +0.64 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[ANAPC10]] | +0.63 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[MRPS22]] | +0.62 | +0.54 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[DDOST]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[PPT1]] | +0.61 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[CIPC]] | +0.60 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[SELENOF]] | +0.60 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[MRPS15]] | +0.60 | +0.50 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[NCSTN]] | +0.60 | +0.51 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[N4BP3]] | -0.62 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[JUND]] | -0.56 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[PAOX]] | -0.56 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[ORAI1]] | -0.56 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[TRAF2]] | -0.55 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[LRRC8E]] | -0.55 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[ARVCF]] | -0.55 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[MIDN]] | -0.55 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[PPP1R35]] ⚠ | -0.55 | -0.48 / -0.53 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NT5C]] | -0.55 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[PIM3]] | -0.55 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[KLF2]] | -0.54 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[EIF5B]] | -0.53 | -0.45 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.573). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-19.9, -15.9); signed map (-19.0, -30.7). **Vector** length 86.0, 16.6% of its response variance represented; |z| ≥ 3 in 868 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.6 | +12.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +19.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.0 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +9.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +3.9 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +6.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +2.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +1.7 | +3.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -4.9 | -4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.1 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.6 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -1.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.8 | -0.8 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | succinate dehydrogenase complex subunit D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.1 — chr11:112,086,824-112,120,016 (+) |
| Ensembl biotype | protein_coding |
| Also known as | cybS; previously PGL, PGL1 |
| Gene groups (HGNC) | Mitochondrial complex II: succinate dehydrogenase subunits |
| Hallmark sets | FATTY_ACID_METABOLISM, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 4 pathways, smallest: Maturation of TCA enzymes and regulation of TCA cycle; Citric acid cycle (TCA cycle); Respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O14521](https://www.uniprot.org/uniprotkb/O14521) (Succinate dehydrogenase):

> Membrane-anchoring subunit of succinate dehydrogenase (SDH) that is involved in complex II of the mitochondrial electron transport chain and is responsible for transferring electrons from succinate to ubiquinone (coenzyme Q). SDH also oxidizes malate to the non-canonical enol form of oxaloacetate, enol-oxaloacetate (By similarity). Enol-oxaloacetate, which is a potent inhibitor of the succinate dehydrogenase activity, is further isomerized into keto-oxaloacetate (By similarity).

**Summary**, from NCBI Gene [6392](https://www.ncbi.nlm.nih.gov/gene/6392):

> This gene encodes a member of complex II of the respiratory chain, which is responsible for the oxidation of succinate. The encoded protein is one of two integral membrane proteins anchoring the complex to the matrix side of the mitochondrial inner membrane. Mutations in this gene are associated with the formation of tumors, including hereditary paraganglioma. Transmission of disease occurs almost exclusively through the paternal allele, suggesting that this locus may be maternally imprinted. …

**Accessions** — [HGNC:10683](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10683) · Entrez [6392](https://www.ncbi.nlm.nih.gov/gene/6392) · UniProt [O14521](https://www.uniprot.org/uniprotkb/O14521) · Ensembl [ENSG00000204370](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204370)

## Data

Gene col 12858: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12858); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12858, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12858]; `tensor/DDL_lfc|DDL_z.npy` [12858]; `embed/gene_vectors.npy` [12858]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12858 or target_col == 12858). Every well: [[SDHD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDHD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
