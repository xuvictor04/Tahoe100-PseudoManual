---
symbol: "TEF"
type: "gene"
col: 9408
ensembl_id: "ENSG00000167074"
name: "TEF transcription factor, PAR bZIP family member"
location: "22q13.2"
module: 14
arm: "+"
pooled_cpm: 6.5
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 19
n_dd_up_clean: 20
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/014", "written"]
generated_by: "tahoemap"
---

# TEF

*TEF transcription factor, PAR bZIP family member* — 22q13.2

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> TEF is a PAR-bZIP transcription factor, one of three clock-output factors with DBP and HLF, found as an activator of the thyrotropin-beta promoter in the embryonic pituitary.

## What it is

TEF (thyrotroph embryonic factor) binds as a homo- or heterodimer to a short TA-rich element shared with DBP, HLF and the repressor [[NFIL3]], which occupies the same site. Cloned from the developing anterior pituitary, where it appears with thyroid-stimulating hormone, it transactivates TSHB; in the adult it is broadly expressed, accumulating on a circadian rhythm in liver and kidney. Function is largely redundant: single knockouts are near-normal, whereas mice lacking DBP, HLF and TEF together develop spontaneous and audiogenic seizures, traced partly to reduced pyridoxal kinase. The three also set the rhythm of hepatic xenobiotic-detoxification genes.

## What is uncertain

Two reasons to discount the rank. The regulon is among the smallest scored, so the score averages a handful of transcripts. And the symbol is treacherous: "TEF-1" was the original name for TEAD1, an unrelated factor, so target sets built from older literature can carry TEAD-derived assignments under this label. Redundancy compounds both: targets attributed to TEF are generally shared with DBP and HLF, and the score cannot separate them.

## References

- Drolet et al., 1991, Genes & Development — cloned TEF from the embryonic anterior pituitary and showed transactivation of the TSHB promoter by a new class of leucine-zipper protein.
- Gachon et al., 2004, Genes & Development — mice lacking DBP, HLF and TEF develop epilepsy, with pyridoxal kinase identified as a target gene.
- Gachon et al., 2006, Cell Metabolism — the circadian PAR-bZIP factors control basal and inducible xenobiotic detoxification.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.13× (z +31.5, q 0e+00, up in 41 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM: 0.331× (z -15.0, q 0e+00, down in 37 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Megestrol (drug)]] 5 µM: 0.543× (z -11.7, q 3e-29, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PER3]] (+0.75, fdr 7e-06), [[REPIN1]] (+0.69, fdr 7e-06), [[TCEANC]] (+0.69, fdr 7e-06); moves opposite to [[AHSA1]] (-0.62, fdr 1e-05), [[MFN1]] (-0.61, fdr 1e-05), [[GPR89A]] (-0.58, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CXXC5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9408.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.13×** | +31.5 | 0e+00 | 41/42 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.42×** | +16.1 | 0e+00 | 39/45 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.45×** | +12.2 | 4e-32 | 26/40 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.83×** | +7.4 | 2e-11 | 22/45 (HEC-1-A, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +6.0 | 3e-07 | 18/46 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.21×** | +5.7 | 1e-06 | 18/40 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +5.0 | 4e-05 | 13/47 (HS-578T, KATO III, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +5.0 | 4e-05 | 14/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +5.0 | 5e-05 | 21/48 (C32, KATO III, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.41×** | +4.7 | 1e-04 | 10/46 (SW480, HS-578T, …) | all doses, flat | position effect removed |
| [[Artesunate (drug)]] 5 µM |  | **1.27×** | +4.7 | 2e-04 | 13/48 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +4.5 | 3e-04 | 14/40 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +4.4 | 4e-04 | 12/43 (SW480, SK-MEL-2, …) | all doses, flat | position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.37×** | +4.3 | 7e-04 | 14/44 (HCT15, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.39×** | +4.2 | 1e-03 | 10/41 (HOP62, SK-MEL-2, …) | all doses, flat | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +4.0 | 0.002 | 11/46 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9408.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | **0.331×** | -15.0 | 0e+00 | 37/47 (HS-578T, A498, …) | rises with dose |  |
| [[Megestrol (drug)]] 5 µM |  | **0.543×** | -11.7 | 3e-29 | 33/48 (A498, Panc 03.27, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.581×** | -7.4 | 3e-11 | 21/44 (SK-MEL-2, CFPAC-1, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.625×** | -6.4 | 2e-08 | 22/45 (A498, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.641×** | -5.8 | 8e-07 | 18/38 (SW480, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.650×** | -5.6 | 2e-06 | 17/39 (HS-578T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.682×** | -5.2 | 2e-05 | 19/47 (H4, HOP62, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Temsirolimus (drug)]] 5 µM |  | **0.779×** | -4.8 | 1e-04 | 12/48 (C-33 A, Panc 03.27, …) | top dose only | position effect removed |
| [[Edoxaban (tosylate monohydrate) (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.708×** | -4.7 | 2e-04 | 15/45 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.736×** | -4.2 | 0.002 | 12/45 (NCI-H1573, A-172, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.558×** | -4.1 | 0.002 | 8/38 (SHP-77, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.750×** | -3.9 | 0.005 | 9/47 (SHP-77, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.750×** | -3.7 | 0.010 | 18/44 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.777×** | -3.4 | 0.025 | 10/46 (H4, NCI-H661, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.838× | -3.4 | 0.027 | 12/47 (H4, HS-578T, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.777×** | -3.3 | 0.032 | 8/45 (HEC-1-A, SK-MEL-2, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.855× | -3.0 | 0.078 | 8/46 (NCI-H1792, PANC-1, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.807×** | -2.9 | 0.096 | 7/47 (NCI-H2347, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9408. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 8.82 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.44× (z +15.9) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.163× (z -10.9) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.310× (z -10.0) |
| [[H4 (line)]] | wt | 10.7 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 7.77× (z +10.3) | [[Ixazomib citrate (drug)]] 5 µM 0.0656× (z -9.6) |
| [[HS-578T (line)]] | alt | 9.48 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.05× (z +14.9) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.114× (z -11.0) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 6.17 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.00× (z +10.2) | [[Proglumide (drug)]] 0.05 µM 0.0682× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 9.35 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +14.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.12 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.05× (z +13.4) | — |
| [[NCI-H1573 (line)]] | alt | 9.11 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +10.9) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.179× (z -8.6) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 10.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.10× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 18.7 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.120× (z -11.2) |
| [[A-172 (line)]] | wt | 7.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.43× (z +12.2) | — |
| [[A549 (line)]] | wt | 1.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 2.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +10.6) | — |
| [[HCT15 (line)]] | alt | 7.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.14× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 13.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +12.0) | — |
| [[Hs 766T (line)]] | wt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.00× (z +14.7) | — |
| [[KATO III (line)]] | alt | 7.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +9.3) | — |
| [[LoVo (line)]] | wt | 4.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 3.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.69× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 8.34 | 0 | 1 | — | [[Megestrol (drug)]] 5 µM 0.230× (z -8.9) |
| [[PANC-1 (line)]] | alt | 5.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +12.1) | — |
| [[SHP-77 (line)]] | alt | 7.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 7.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +9.0) | — |
| [[SW480 (line)]] | alt | 6.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +9.3) | — |
| [[A-427 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9408), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PER3]] | +0.75 | +0.72 / +0.73 | both halves | 7e-06 | STRING 822 |
| [[REPIN1]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[TCEANC]] | +0.69 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[ZFHX2]] | +0.69 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[PBX2]] | +0.68 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[BHLHE41]] | +0.68 | +0.69 / +0.64 | both halves | 7e-06 | STRING 534 |
| [[SYNPO]] | +0.68 | +0.71 / +0.57 | both halves | 8e-06 |  |
| [[BCL3]] | +0.68 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[SYNGAP1]] | +0.67 | +0.71 / +0.58 | both halves | 8e-06 |  |
| [[ARHGEF40]] | +0.65 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[CX3CL1]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[SOCS2]] | +0.65 | +0.62 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHSA1]] | -0.62 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[MFN1]] | -0.61 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[GPR89A]] | -0.58 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[ZCCHC17]] | -0.58 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[RAP1GDS1]] | -0.57 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[STRAP]] | -0.57 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.57 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[DCAF13]] | -0.57 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ZDHHC9]] | -0.56 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[POP1]] | -0.56 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[FAM135A]] | -0.56 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[PIGF]] | -0.55 | -0.51 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXXC5]] | B | CXXC5 activity raises TEF's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 1.59× lower at baseline in the lines without CXXC5 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[ADGRG1]] | B | ADGRG1 activity raises TEF's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 1.49× lower at baseline in the lines without ADGRG1 | 0.039 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[ADGRG1]] | B | ADGRG1 activity strengthens TEF's drug response | lines that do not express ADGRG1 (12) vs lines expressing it (36) | the lines without ADGRG1 respond 0.48× as strongly (z diff +1.67); rises at some drug-doses, falls at others (32% from rises): Megestrol 5 µM: 0.75x vs 0.49x (z diff +2.7); Edoxaban (tosylate monohydrate) 5 µM: 0.47x vs 0.29x (z diff +2.5); Homoharringtonine 5 µM: 4.59x vs 5.06x (z diff +2.0) | 0.054 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526; target measured in part of the lines; rises at some drug-doses, falls at others; line-wide correction only; artifact flags |
| [[LGALS3]] | B | LGALS3 activity strengthens TEF's drug response | lines that do not express LGALS3 (11) vs lines expressing it (37) | the lines without LGALS3 respond 0.40× as strongly (z diff +1.49); strongest at Megestrol 5 µM: 0.85x vs 0.48x (z diff +3.0) | 0.085 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1; target measured in part of the lines; line-wide correction only; artifact flags |
| [[ZNF20]] | C | ZNF20 activity raises TEF's level | lines that do not express ZNF20 (4) vs lines expressing it (46) | 1.70× lower at baseline in the lines without ZNF20 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000268870, ZNF700, ZNF44; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.713). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.0, 5.2); signed map (28.6, 7.4). **Vector** length 81.8, 14.5% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.7 | +31.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.8 | +16.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.3 | +12.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.6 | +6.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.3 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +4.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.1 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +1.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.9 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -7.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.5 | -3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -5.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -6.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | TEF transcription factor, PAR bZIP family member |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:41,367,333-41,399,326 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1655 |
| Gene groups (HGNC) | PAR bZIP family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q10587](https://www.uniprot.org/uniprotkb/Q10587) (Thyrotroph embryonic factor):

> Transcription factor that binds to and transactivates the TSHB promoter. Binds to a minimal DNA-binding sequence 5'-[TC][AG][AG]TTA[TC][AG]-3'.

**Summary**, from NCBI Gene [7008](https://www.ncbi.nlm.nih.gov/gene/7008):

> This gene encodes a member of the PAR (proline and acidic amino acid-rich) subfamily of basic region/leucine zipper (bZIP) transcription factors. It is expressed in a broad range of cells and tissues in adult animals, however, during embryonic development, TEF expression appears to be restricted to the developing anterior pituitary gland, coincident with the appearance of thyroid-stimulating hormone, beta (TSHB). Indeed, TEF can bind to, and transactivate the TSHB promoter. It shows homology …

**Accessions** — [HGNC:11722](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11722) · Entrez [7008](https://www.ncbi.nlm.nih.gov/gene/7008) · UniProt [Q10587](https://www.uniprot.org/uniprotkb/Q10587) · Ensembl [ENSG00000167074](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167074)

## Data

Gene col 9408: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9408); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9408, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9408]; `tensor/DDL_lfc|DDL_z.npy` [9408]; `embed/gene_vectors.npy` [9408]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9408 or target_col == 9408). Every well: [[TEF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/TEF.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
