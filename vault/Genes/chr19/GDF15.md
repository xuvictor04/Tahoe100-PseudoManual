---
symbol: "GDF15"
type: "gene"
col: 5073
ensembl_id: "ENSG00000130513"
name: "growth differentiation factor 15"
location: "19p13.11"
module: 62
arm: "+"
pooled_cpm: 59.33
n_lines_expressing: 32
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/062", "written"]
generated_by: "tahoemap"
---

# GDF15

*growth differentiation factor 15* — 19p13.11

> [!summary] In one line
> GDF15 encodes a secreted, divergent TGF-β superfamily cytokine that signals through a single receptor in the hindbrain to suppress appetite, and that p53 induces — along with almost every other kind of cellular stress.

## What it is

GDF15 has an unusual number of names — MIC-1, NAG-1, PLAB, PTGF-β, PDF — because several groups found it independently in unrelated screens, itself a clue to how promiscuously it is induced. It is a distant TGF-β superfamily member, secreted as a disulfide-linked dimer after pro-protein cleavage. Basal expression is low in most tissues and high in placenta; levels rise steeply with injury, inflammation, mitochondrial dysfunction, renal and cardiac disease, ageing and cancer. It is among the strongest single-protein predictors of all-cause mortality — a general distress signal, not a disease marker.

Its receptor was a long-standing puzzle, resolved in 2017 when four groups independently identified GFRAL, an orphan GDNF-family receptor that uses RET as co-receptor and is expressed essentially only in the area postrema and nucleus tractus solitarius. That anatomy explains the physiology: GDF15 acts on brainstem circuitry for nausea and aversion, suppressing food intake and causing weight loss — now understood as a principal effector arm of cancer cachexia. Metformin's weight effect runs substantially through GDF15, and GDF15 is linked to nausea and vomiting of pregnancy.

Its transcriptional control is where this gene earns its caution. GDF15 was identified as a p53 target gene and proposed as a serum biomarker of p53 pathway activation. But it is also induced strongly by the ATF4/CHOP integrated stress response, by mitochondrial dysfunction, by inflammatory cytokines, and — the original NAG-1 finding — by NSAIDs independent of cyclooxygenase. Several largely independent stress pathways converge on this one promoter.

## What is uncertain

Whether p53 acts at the GDF15 promoter directly or through the stress machinery p53 activation itself engages is not settled in a way I would rely on: a p53 response element has been reported here, but the ATF4 route is at least as strong in many systems, and in some contexts GDF15 is induced with no p53 requirement at all. So "p53 target" is true but far from exclusive, and GDF15 induction is weak evidence that p53 specifically is on. Its direction of effect in cancer is genuinely contested, not merely unresolved: the NAG-1 literature describes it as pro-apoptotic and antitumorigenic, the cachexia literature as a driver of poor outcome; the resolution is probably that early cell-autonomous and late systemic effects differ. Its expression here is low enough that per-cell measurement is noisy, limiting what any single-cell correlation can establish.

## References

- Tan et al., 2000, PNAS — identified PTGF-β/GDF15 as a p53 target gene inhibiting tumour cell growth through TGF-β signalling.
- Baek et al., 2001, Molecular Pharmacology — cyclooxygenase inhibitors induce this TGF-β superfamily member (NAG-1), independent of COX, with proapoptotic and antitumorigenic activity.
- Yang et al., 2003, Molecular Cancer Therapeutics — proposed MIC-1/GDF15 as a biomarker of p53 pathway activation.
- Mullican et al., 2017, Nature Medicine, and Hsu et al., 2017, Nature — identified GFRAL as the GDF15 receptor and localised it to the area postrema and nucleus tractus solitarius.
- Coll et al., 2020, Nature — showed GDF15 mediates the effects of metformin on body weight and energy balance.
- Lockhart et al., 2020, Endocrine Reviews — review framing GDF15 as a hormone conveying somatic distress to the brain.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 2.17× (z +5.4, q 5e-05, up in 21 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.495× (z -4.7, q 0.002, down in 18 of 30 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (HT-29 0.160×, LoVo 0.233×, H4 0.104×, LS 180 0.197×, …); [[Panobinostat (drug)]] 0.5 µM in 4 lines (LoVo 0.0874×, LS 180 0.117×, H4 0.0539×, C32 0.116×); [[Panobinostat (drug)]] 5 µM in 3 lines (LoVo 0.0712×, C32 0.105×, SW48 0.0371×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACER2]] (+0.70, fdr 1e-05), [[PINCR]] (+0.68, fdr 7e-06), [[TNFRSF10B]] (+0.65, fdr 1e-05); moves opposite to [[PRC1]] (-0.48, fdr 8e-05), [[TMPO]] (-0.48, fdr 7e-05), [[ELAC2]] (-0.48, fdr 4e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NUPR1]] → it (grade B ⚠); 3 go from it, the strongest it → [[EIF2S2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5073.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM |  | **2.17×** | +5.4 | 5e-05 | 21/30 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.13×** | +5.2 | 5e-05 | 17/30 (A549, A498, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.64×** | +4.8 | 3e-04 | 19/30 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.96×** | +4.6 | 5e-04 | 19/28 (A-172, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +4.4 | 0.001 | 18/30 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +4.2 | 0.002 | 14/29 (A498, C32, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.83×** | +4.2 | 0.002 | 15/29 (HEC-1-A, SHP-77, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.83×** | +4.2 | 0.002 | 19/30 (NCI-H2347, SHP-77, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.51×** | +4.0 | 0.004 | 19/30 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.71×** | +3.7 | 0.012 | 23/29 (HEC-1-A, H4, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +3.5 | 0.021 | 13/29 (H4, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 5 µM |  | **1.61×** | +3.1 | 0.078 | 13/30 (A498, HT-29, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.078 | 15/30 (LS 180, A498, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 1.36× | +3.0 | 0.11 | 19/31 (NCI-H460, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5073.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (HT-29 0.160×, LoVo 0.233×, H4 0.104×, LS 180 0.197×, …); [[Panobinostat (drug)]] 0.5 µM in 4 lines (LoVo 0.0874×, LS 180 0.117×, H4 0.0539×, C32 0.116×); [[Panobinostat (drug)]] 5 µM in 3 lines (LoVo 0.0712×, C32 0.105×, SW48 0.0371×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.495×** | -4.7 | 0.002 | 18/30 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.670×** | -3.9 | 0.025 | 18/29 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | 0.701× | -3.4 | 0.11 | 19/30 (SHP-77, PANC-1, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.576× | -3.4 | 0.11 | 16/30 (CFPAC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.611× | -3.3 | 0.12 | 19/29 (C32, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5073. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 254 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0712× (z -15.9) |
| [[LS 180 (line)]] | wt | 205 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -12.2) |
| [[SW48 (line)]] | wt | 135 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.0371× (z -11.4) |
| [[H4 (line)]] | wt | 169 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -12.3) |
| [[HT-29 (line)]] | alt | 99.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -16.8) |
| [[C32 (line)]] | wt | 365 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -11.6) |
| [[KATO III (line)]] | alt | 33.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -11.0) |
| [[SHP-77 (line)]] | alt | 22.2 | 1 | 2 (1 ⚠) | [[Retinoic acid (drug)]] 5 µM 4.78× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -10.2) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.205× (z -9.1) |
| [[PANC-1 (line)]] | alt | 38.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -10.8) |
| [[A-172 (line)]] | wt | 83.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 9.35× (z +8.8) | — |
| [[A498 (line)]] | wt | 273 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 5.23× (z +8.9) | — |
| [[A549 (line)]] | wt | 29.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 6.48× (z +9.1) | — |
| [[CHP-212 (line)]] | wt | 118 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0945× (z -11.2) |
| [[COLO 205 (line)]] | alt | 68.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -9.4) ⚠ cell-cycle shift, explains ~5% of this change |
| [[NCI-H2347 (line)]] | alt | 19.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.84× (z +10.4) | — |
| [[NCI-H460 (line)]] | wt | 25.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.107× (z -8.5) |
| [[SW1417 (line)]] | alt | 94.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -13.3) ⚠ cell-cycle shift, explains ~5% of this change |
| [[A-427 (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.20 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.31 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 215 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.43 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.52 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.32 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 11.4 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.01 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.83 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.33 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.57 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.26 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.52 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.11 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 34.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5073), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACER2]] | +0.70 | +0.55 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[PINCR]] | +0.68 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[TNFRSF10B]] | +0.65 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[ISCU]] | +0.61 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[GRIN2C]] | +0.60 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[CDKN1A]] | +0.59 | +0.47 / +0.64 | both halves | 2e-05 | STRING 556 |
| [[BEX2]] | +0.59 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[FDXR]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 | STRING 411 |
| [[PGPEP1]] | +0.58 | +0.58 / +0.72 | both halves | 8e-06 | ⚠ same locus (4.8 kb, same strand: neighbours can correlate without regulation) |
| [[RPS27L]] | +0.58 | +0.38 / +0.65 | both halves | 7e-05 |  |
| [[DNAI3]] | +0.58 | +0.19 / +0.69 | ⚠ one half (not replicated) | 8e-04 |  |
| [[DYRK3]] | +0.58 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[EDA2R]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[DDIT3]] | +0.55 | +0.45 / +0.60 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRC1]] | -0.48 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[TMPO]] | -0.48 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[ELAC2]] | -0.48 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[LMNB2]] | -0.48 | -0.33 / -0.52 | both halves | 1e-04 | same gene group |
| [[SLC25A24]] | -0.47 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[HASPIN]] | -0.47 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[FOXM1]] | -0.47 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[NUP188]] | -0.46 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[MCM4]] | -0.46 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[KIF11]] | -0.45 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[LMNB1]] | -0.45 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[TTF2]] | -0.45 | -0.32 / -0.57 | both halves | 2e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUPR1]] | B | NUPR1 activity raises GDF15's level | lines that do not express NUPR1 (24) vs lines expressing it (26) | 2.91× lower at baseline in the lines without NUPR1 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TTTY14, SPARC, PCDH18 |
| [[PINCR]] | B | PINCR activity strengthens GDF15's drug response | lines that do not express PINCR (15) vs lines expressing it (15) | the lines without PINCR respond 0.72× as strongly (z diff +0.71); strongest at Idarubicin (hydrochloride) 0.5 µM: 1.45x vs 4.45x (z diff +3.9) | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; both ways; artifact flags |
| [[TP53]] | B | TP53 activity strengthens GDF15's drug response | recorded loss-of-function mutation of TP53 in 17 lines vs 13 not recorded | the TP53-altered lines respond 0.70× as strongly (z diff +0.85); strongest at Idarubicin (hydrochloride) 0.5 µM: 1.44x vs 5.33x (z diff +4.6) | 0.091 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; both ways; the reference differs; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EIF2S2]] | B | GDF15 activity lowers EIF2S2's level | lines that do not express GDF15 (18) vs lines expressing it (32) | 1.06× higher at baseline in the lines without GDF15 | 0.041 | ⚠ within organs, on part of the lines; also absent: PCSK5, ALOX5, LINC03040 |
| [[PTCHD4]] | B | GDF15 activity raises PTCHD4's level | lines that do not express GDF15 (18) vs lines expressing it (32) | 2.58× lower at baseline in the lines without GDF15 | 0.069 | ⚠ within organs, on part of the lines; also absent: PCSK5, ALOX5, LINC03040 |
| [[TP53INP1]] | B | GDF15 activity raises TP53INP1's level | lines that do not express GDF15 (18) vs lines expressing it (32) | 1.36× lower at baseline in the lines without GDF15 | 0.078 | ⚠ within organs, on part of the lines; also absent: PCSK5, ALOX5, LINC03040 |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.620). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.8, 38.0); signed map (44.4, -22.7). **Vector** length 107, 34.5% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.6 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +6.5 | +5.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +4.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.6 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +4.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.5 | +3.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.4 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.2 | -2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.8 | -3.4 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | growth differentiation factor 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,374,731-18,389,176 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PLAB, MIC-1, PDF, MIC1, NAG-1, PTGFB |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Transforming growth factor beta superfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99988](https://www.uniprot.org/uniprotkb/Q99988) (Growth/differentiation factor 15):

> Hormone produced in response to various stresses to confer information about those stresses to the brain, and trigger an aversive response, characterized by nausea, vomiting, and/or loss of appetite. The aversive response is both required to reduce continuing exposure to those stresses at the time of exposure and to promote avoidance behavior in the future. Acts by binding to its receptor, GFRAL, activating GFRAL-expressing neurons localized in the area postrema and nucleus tractus solitarius …

**Summary**, from NCBI Gene [9518](https://www.ncbi.nlm.nih.gov/gene/9518):

> This gene encodes a secreted ligand of the TGF-beta (transforming growth factor-beta) superfamily of proteins. Ligands of this family bind various TGF-beta receptors leading to recruitment and activation of SMAD family transcription factors that regulate gene expression. The encoded preproprotein is proteolytically processed to generate each subunit of the disulfide-linked homodimer. The protein is expressed in a broad range of cell types, acts as a pleiotropic cytokine and is involved in the …

**Accessions** — [HGNC:30142](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30142) · Entrez [9518](https://www.ncbi.nlm.nih.gov/gene/9518) · UniProt [Q99988](https://www.uniprot.org/uniprotkb/Q99988) · Ensembl [ENSG00000130513](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130513)

## Data

Gene col 5073: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5073); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5073, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5073]; `tensor/DDL_lfc|DDL_z.npy` [5073]; `embed/gene_vectors.npy` [5073]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5073 or target_col == 5073). Every well: [[GDF15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/GDF15.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
